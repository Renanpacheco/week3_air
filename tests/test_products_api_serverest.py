import pytest
import requests
import time
from dotenv import load_dotenv
import os

pytestmark = pytest.mark.skip(reason="Tests off temporarily")

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.fixture
def token_autentication():
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]

@pytest.mark.skip()
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

@pytest.mark.skip()
def test_list_products():
    response = requests.get(f"{BASE_URL}/produtos")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0