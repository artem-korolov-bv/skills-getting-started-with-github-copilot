"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    """Provide a test client for API route testing."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep in-memory activity data isolated between tests."""
    snapshot = deepcopy(activities)
    yield
    activities.clear()
    activities.update(deepcopy(snapshot))
