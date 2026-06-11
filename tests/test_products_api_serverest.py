import pytest
import requests
import time

BASE_URL = "https://compassuol.serverest.dev"

@pytest.fixture
def token_autentication():
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]

def test_login_success():
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert body["message"] == "Login realizado com sucesso"
    assert "authorization" in body


def test_create_product(token_autentication):
    
    headers = {
        "Authorization": token_autentication
    }
    
    name_product = f"mouse{int(time.time() * 1000)}"
    payload = {
        "nome": name_product,
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.post(f"{BASE_URL}/produtos", headers=headers, json=payload)
    assert response.status_code == 201
    
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert isinstance(body["_id"], str)