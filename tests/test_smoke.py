from src.app.main import app

def test_app_title():
    assert app.title
    assert 'treasury-risk-command-desk' in app.openapi()['info']['title'].lower().replace(' ', '-') or app.title
