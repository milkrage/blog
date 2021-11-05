import pytest

from blog import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        return client
