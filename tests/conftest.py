import pytest

from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    client = app.test_client()
    with app.app_context():
        yield client