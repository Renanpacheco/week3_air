import pytest
import requests
import time
from dotenv import load_dotenv
import os
from jsonschema import validate
from schemas.cart_schema import cart_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.mark.skip()
def test_list_carts():
    response = requests.get(f"{BASE_URL}/carrinhos")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0

def test_get_cart_by_id():

    #id_cart = register_cart["_id"]
    id_cart = "qbMqntef4iTOwWfg"

    response = requests.get(f"{BASE_URL}/carrinhos/{id_cart}")

    assert response.status_code == 200

    body = response.json()

    validate(instance=body, schema=cart_schema)


def test_create_cart_without_token():
    payload = {
        "nome": "carrinho 024578",
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }
    response = requests.post(f"{BASE_URL}/carrinhos", json=payload)
    assert response.status_code == 401
    body = response.json()    
    assert body["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"


def test_create_cart_with_invalid_token():
    
    headers = {
        "Authorization": "bearer invalid_token"
    }
    
    name_product = f"mouse{int(time.time() * 1000)}"
    payload = {
        "nome": name_product,
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.post(f"{BASE_URL}/produtos", headers=headers, json=payload)
    assert response.status_code == 401
    
    body = response.json()
    assert body["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

@pytest.mark.skip()    
def test_create_cart_without_name(token_autentication):
    headers = {
        "Authorization": token_autentication
    }
    
    payload = {
        
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }
    
    response = requests.post(f"{BASE_URL}/produtos", headers=headers, json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["nome"] == "nome é obrigatório"

