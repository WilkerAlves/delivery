import pytest
from delivery.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instancia do app flask"""
    return create_app()