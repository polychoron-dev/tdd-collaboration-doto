import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_google_login_redirect():
    response = client.get("/auth/google/login")
    
    assert response.status_code == 302

    location = response.headers.get("location")
    assert location is not None
    assert "accounts.google.com" in location



class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json

# ダミーのHTTP POST関数を作成し、token exchange (トークン交換) 処理を模倣する
@pytest.fixture(autouse=True)
def override_httpx_async_post(monkeypatch):
    async def dummy_post(*args, **kwargs):
        dummy_data = {
            "access_token": "dummy_access_token",
            "expires_in": 3600,
            "scope": "openid email profile",
            "token_type": "Bearer",
            "id_token": "dummy_id_token"
        }
        return DummyResponse(200, dummy_data)
    monkeypatch.setattr("httpx.AsyncClient.post", dummy_post)

def test_google_callback_redirect():
    # コード（dummy_code）をクエリパラメータとして渡してエンドポイントを呼び出す
    response = client.get("/auth/google/callback", params={"code": "dummy_code"})
    
    assert response.status_code in (302, 307)
    assert response.headers.get("location") == "/" # ルートにリダイレクト