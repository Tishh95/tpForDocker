import pytest
from pymongo import MongoClient


@pytest.fixture
def client():
    return app.test_client()
