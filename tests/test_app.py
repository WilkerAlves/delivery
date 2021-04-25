# esse parametro app vem atravez da conftest
def test_app_is_create(app):
    assert app.name ==  "delivery.app"

# esse parametro config é provido pelo pytest-flask que está instalado
def test_config_is_loaded(config):
    assert config['DEBUG'] is False

# esse parametro client é provido pelo pytest-flask que está instalado
def test_request_returns_404(client):
    assert client.get("/url_que_nao_existe").status_code == 404
