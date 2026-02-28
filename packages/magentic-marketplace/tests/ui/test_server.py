"""Tests for the UI server module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from magentic_marketplace.ui import server


@pytest.fixture(autouse=True)
def _reset_cache():
    """Reset the marketplace data cache before each test."""
    server._marketplace_data_cache = None
    yield
    server._marketplace_data_cache = None


def _make_customer_agent_row(agent_id: str, name: str):
    """Create a mock agent row for a customer."""
    row = MagicMock()
    row.id = agent_id
    row.data.model_dump.return_value = {
        "id": agent_id,
        "metadata": {"type": "customer"},
        "customer": {
            "type": "customer",
            "id": agent_id,
            "name": name,
            "request": "Looking for good food",
            "menu_features": {"pizza": 15.0},
            "amenity_features": ["delivery"],
        },
    }
    return row


def _make_business_agent_row(agent_id: str, name: str):
    """Create a mock agent row for a business."""
    row = MagicMock()
    row.id = agent_id
    row.data.model_dump.return_value = {
        "id": agent_id,
        "metadata": {"type": "business"},
        "business": {
            "type": "business",
            "id": agent_id,
            "name": name,
            "description": "A great restaurant",
            "rating": 4.5,
            "progenitor_customer": "customer_000",
            "menu_features": {"pizza": 12.0, "pasta": 10.0},
            "amenity_features": {"delivery": True, "wifi": False},
            "min_price_factor": 0.8,
        },
    }
    return row


class TestLoadAgents:
    """Tests for the _load_agents function."""

    @pytest.mark.asyncio
    async def test_load_agents_returns_customers_and_businesses(self):
        """Test that _load_agents splits agents into customers and businesses."""
        mock_db = MagicMock()
        mock_db.agents.get_all = AsyncMock(
            return_value=[
                _make_customer_agent_row("c1", "Alice"),
                _make_business_agent_row("b1", "Pizza Place"),
                _make_customer_agent_row("c2", "Bob"),
            ]
        )

        with patch.object(server, "_db_controller", mock_db):
            customers, businesses = await server._load_agents()

        assert len(customers) == 2
        assert len(businesses) == 1
        assert customers[0]["id"] == "c1"
        assert customers[0]["name"] == "Alice"
        assert customers[1]["id"] == "c2"
        assert businesses[0]["id"] == "b1"
        assert businesses[0]["name"] == "Pizza Place"
        assert businesses[0]["rating"] == 4.5

    @pytest.mark.asyncio
    async def test_load_agents_empty_database(self):
        """Test _load_agents with no agents in the database."""
        mock_db = MagicMock()
        mock_db.agents.get_all = AsyncMock(return_value=[])

        with patch.object(server, "_db_controller", mock_db):
            customers, businesses = await server._load_agents()

        assert customers == []
        assert businesses == []

    @pytest.mark.asyncio
    async def test_load_agents_raises_without_db(self):
        """Test _load_agents raises RuntimeError when db is not initialized."""
        with patch.object(server, "_db_controller", None):
            with pytest.raises(
                RuntimeError, match="Database controller not initialized"
            ):
                await server._load_agents()

    @pytest.mark.asyncio
    async def test_load_agents_business_price_range(self):
        """Test that business price_min and price_max are computed correctly."""
        mock_db = MagicMock()
        mock_db.agents.get_all = AsyncMock(
            return_value=[_make_business_agent_row("b1", "Pizza Place")]
        )

        with patch.object(server, "_db_controller", mock_db):
            _customers, businesses = await server._load_agents()

        assert businesses[0]["price_min"] == 10.0
        assert businesses[0]["price_max"] == 12.0


class TestCreateMessageThreads:
    """Tests for the _create_message_threads function."""

    def test_text_message_creates_thread(self):
        """Test that a text message creates a thread between customer and business."""
        customers = [{"id": "c1", "name": "Alice"}]
        businesses = [{"id": "b1", "name": "Pizza Place"}]
        messages = [
            {
                "id": "msg1",
                "from_agent": "c1",
                "to_agent": "b1",
                "type": "text",
                "content": "Hello",
                "created_at": "2024-01-01T00:00:00",
            }
        ]

        threads, payments = server._create_message_threads(
            customers, businesses, messages
        )

        assert "c1-b1" in threads
        assert len(threads["c1-b1"]["messages"]) == 1
        assert threads["c1-b1"]["participants"]["customer"]["id"] == "c1"
        assert threads["c1-b1"]["participants"]["business"]["id"] == "b1"
        assert len(payments) == 0

    def test_payment_message_tracked(self):
        """Test that payment messages are tracked in threads_with_payments."""
        customers = [{"id": "c1", "name": "Alice"}]
        businesses = [{"id": "b1", "name": "Pizza Place"}]
        messages = [
            {
                "id": "msg1",
                "from_agent": "c1",
                "to_agent": "b1",
                "type": "payment",
                "content": {"amount": 15.0},
                "created_at": "2024-01-01T00:00:00",
            }
        ]

        threads, payments = server._create_message_threads(
            customers, businesses, messages
        )

        assert "c1-b1" in payments

    def test_search_message_creates_threads_for_matched_businesses(self):
        """Test that search messages create threads for all matched businesses."""
        customers = [{"id": "c1", "name": "Alice"}]
        businesses = [
            {"id": "b1", "name": "Pizza Place"},
            {"id": "b2", "name": "Sushi Bar"},
        ]
        messages = [
            {
                "id": "msg1",
                "from_agent": "c1",
                "to_agent": None,
                "type": "search",
                "content": {"type": "search", "query": "food"},
                "created_at": "2024-01-01T00:00:00",
                "business_ids": ["b1", "b2"],
            }
        ]

        threads, _payments = server._create_message_threads(
            customers, businesses, messages
        )

        assert "c1-b1" in threads
        assert "c1-b2" in threads

    def test_empty_messages_returns_empty(self):
        """Test with no messages returns empty results."""
        threads, payments = server._create_message_threads([], [], [])

        assert threads == {}
        assert payments == set()

    def test_multiple_messages_same_thread(self):
        """Test that multiple messages between same pair go to same thread."""
        customers = [{"id": "c1", "name": "Alice"}]
        businesses = [{"id": "b1", "name": "Pizza Place"}]
        messages = [
            {
                "id": "msg1",
                "from_agent": "c1",
                "to_agent": "b1",
                "type": "text",
                "content": "Hello",
                "created_at": "2024-01-01T00:00:00",
            },
            {
                "id": "msg2",
                "from_agent": "b1",
                "to_agent": "c1",
                "type": "text",
                "content": "Hi there!",
                "created_at": "2024-01-01T00:01:00",
            },
        ]

        threads, _payments = server._create_message_threads(
            customers, businesses, messages
        )

        assert len(threads) == 1
        assert len(threads["c1-b1"]["messages"]) == 2
        assert threads["c1-b1"]["lastMessageTime"] == "2024-01-01T00:01:00"


class TestMarketplaceDataCache:
    """Tests for the marketplace data caching behavior."""

    @pytest.mark.asyncio
    async def test_cache_returns_cached_data(self):
        """Test that cached data is returned without hitting the database."""
        cached = {"messages": [], "messageThreads": [], "analytics": {}}
        server._marketplace_data_cache = cached

        app = server.create_analytics_app("test_schema")

        # Find the get_marketplace_data route handler
        for route in app.routes:
            if hasattr(route, "path") and route.path == "/api/marketplace-data":
                # Call the endpoint function directly
                result = await route.endpoint()
                assert result is cached
                break

    @pytest.mark.asyncio
    async def test_cache_is_none_initially(self):
        """Test that cache starts as None."""
        assert server._marketplace_data_cache is None


class TestCreateAnalyticsApp:
    """Tests for the create_analytics_app function."""

    def test_creates_fastapi_app(self):
        """Test that create_analytics_app returns a FastAPI application."""
        app = server.create_analytics_app("test_schema")
        assert app.title == "Marketplace UI API"

    def test_app_has_required_routes(self):
        """Test that the app has all required API routes."""
        app = server.create_analytics_app("test_schema")
        route_paths = [route.path for route in app.routes if hasattr(route, "path")]

        assert "/api" in route_paths
        assert "/api/customers" in route_paths
        assert "/api/businesses" in route_paths
        assert "/api/marketplace-data" in route_paths
        assert "/api/health" in route_paths

    def test_cors_middleware_configured(self):
        """Test that CORS middleware is configured."""
        app = server.create_analytics_app("test_schema")
        middleware_classes = [type(m).__name__ for m in app.user_middleware]
        assert "Middleware" in str(middleware_classes) or len(app.user_middleware) > 0
