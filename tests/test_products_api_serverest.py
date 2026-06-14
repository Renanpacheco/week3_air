import pytest
import requests
import time
from dotenv import load_dotenv
import os
from jsonschema import validate
from schemas.product_schema import product_schema

load_dotenv()



BASE_URL = os.getenv("BASE_URL")

pytestmark = pytest.mark.skip(reason="Tests off temporarily")

@pytest.fixture
def generate_name_product():
    
    return f"mouse{int(time.time() * 1000)}"

@pytest.fixture
def token_autentication():
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]

@pytest.fixture
def register_product(token_autentication, generate_name_product):
    
    headers = {
        "Authorization": token_autentication
    }
    
    
    payload = {
        "nome": generate_name_product,
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.post(f"{BASE_URL}/produtos", headers=headers, json=payload)
    assert response.status_code == 201
    
    product_date = response.json()
    product_date["used_name"] = generate_name_product
    
    yield product_date
    
    requests.delete(f"{BASE_URL}/produtos/{product_date['_id']}")
    
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert isinstance(body["_id"], str)

@pytest.mark.skip()    
def test_create_product_with_duplicate_name(token_autentication, register_product):#remenber to get a product to test for indenpende of this test
    headers = {
        "Authorization": token_autentication
    }
    
    
    payload = {
        "nome": register_product["used_name"],
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.post(f"{BASE_URL}/produtos", headers=headers, json=payload)
    assert response.status_code == 400
    
    body = response.json()
    assert body["message"] == "Já existe produto com esse nome"

@pytest.mark.skip()
def test_list_products():
    response = requests.get(f"{BASE_URL}/produtos")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0


@pytest.mark.skip()
def test_create_product_without_token():
    payload = {
        "nome": "mouse",
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }
    response = requests.post(f"{BASE_URL}/produtos", json=payload)
    assert response.status_code == 401
    body = response.json()    
    assert body["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

@pytest.mark.skip()
def test_create_product_with_invalid_token():
    
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
def test_create_product_without_name(token_autentication):
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

@pytest.mark.skip()    
def test_get_product_by_id():

    id_product = "BeeJh5lz3k6kSIzA"

    response = requests.get(f"{BASE_URL}/produtos/{id_product}")

    assert response.status_code == 200

    body = response.json()

    validate(instance=body, schema=product_schema)

@pytest.mark.skip()
def test_update_product(register_product, token_autentication):
    id_product = register_product["_id"]
    
    
    headers = {
        "Authorization": token_autentication
    }

    name_product = f"update{int(time.time() * 1000)}"
    payload = {
        "nome": name_product,
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.put(f"{BASE_URL}/produtos/{id_product}", headers=headers, json=payload)
    assert response.status_code == 200

    body = response.json()
    assert body["message"] == "Registro alterado com sucesso"

@pytest.mark.skip()
def test_delete_product(register_product, token_autentication):
    
    id_product = register_product["_id"]
    
    headers = {
        "Authorization": token_autentication
    }
    
    response = requests.delete(f"{BASE_URL}/produtos/{id_product}", headers=headers)
    assert response.status_code == 200

    body = response.json()
    assert body["message"] == "Registro excluído com sucesso"