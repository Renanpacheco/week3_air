import pytest
import requests
import time
from dotenv import load_dotenv
import os
from jsonschema import validate
from schemas.cart_schema import cart_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

'''@pytest.fixture
def token_autentication():
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]
'''
@pytest.fixture
def create_product(token_autentication):

    headers = {
        "Authorization": token_autentication
    }

    product_name = f"Produto {int(time.time() * 1000)}"

    payload = {
        "nome": product_name,
        "preco": 100,
        "descricao": "Produto para teste",
        "quantidade": 10
    }

    response = requests.post(
        f"{BASE_URL}/produtos",
        headers=headers,
        json=payload
    )

    assert response.status_code == 201

    yield response.json()

    requests.delete(
        f"{BASE_URL}/produtos/{response.json()['_id']}",
        headers=headers
    )

@pytest.fixture
def token_autentication(create_user):

    payload = {
        "email": create_user["email"],
        "password": create_user["password"]
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    assert response.status_code == 200

    return response.json()["authorization"]

@pytest.fixture
def create_user():

    email = f"renan{int(time.time() * 1000)}@teste.com"

    payload = {
        "nome": "Renan",
        "email": email,
        "password": "teste",
        "administrador": "true"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 201

    user = response.json()

    yield {
        "_id": user["_id"],
        "email": email,
        "password": "teste"
    }

    requests.delete(
        f"{BASE_URL}/usuarios/{user['_id']}"
    )


@pytest.mark.skip()
def test_list_carts():
    response = requests.get(f"{BASE_URL}/carrinhos")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0

@pytest.mark.skip()
def test_get_cart_by_id():

    #id_cart = register_cart["_id"]
    id_cart = "qbMqntef4iTOwWfg"

    response = requests.get(f"{BASE_URL}/carrinhos/{id_cart}")

    assert response.status_code == 200

    body = response.json()

    validate(instance=body, schema=cart_schema)

@pytest.mark.skip()
def test_get_cart_nonexistent():

    
    id_cart = "qbMqntef4iTOwWfa"

    response = requests.get(f"{BASE_URL}/carrinhos/{id_cart}")

    assert response.status_code == 400

    body = response.json()
    assert body["message"] == "Carrinho não encontrado"
    
@pytest.mark.skip()
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

@pytest.mark.skip()
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
def test_create_second_cart(token_autentication):
    
    headers = {
        "Authorization": token_autentication
    }
    
    payload = {
        "produtos": [
            {
                "idProduto": "2RjZPVeOIOXtTDGK",
                "quantidade": 2
            }
        ]
    }

    
    response = requests.post(f"{BASE_URL}/carrinhos", headers=headers, json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["message"] == "Não é permitido ter mais de 1 carrinho"


@pytest.mark.skip() 
def test_create_cart_empty(token_autentication):
    headers = {
        "Authorization": token_autentication
    }
    
    payload = {
        
    }
    
    response = requests.post(f"{BASE_URL}/carrinhos", headers=headers, json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["produtos"] == "produtos é obrigatório"

@pytest.mark.skip()
def test_create_cart(token_autentication, create_product):

    headers = {
        "Authorization": token_autentication
    }

    payload = {
        "produtos": [
            {
                "idProduto": create_product["_id"],
                "quantidade": 2
            }
        ]
    }

    response = requests.post(
        f"{BASE_URL}/carrinhos",
        headers=headers,
        json=payload
    )

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Cadastro realizado com sucesso"
    

def test_buy_cart(token_autentication, create_product):

    headers = {
        "Authorization": token_autentication
    }
    
    product_id = create_product["_id"]
    response = requests.get(f"{BASE_URL}/produtos/{product_id}")

    stock_before = response.json()["quantidade"]

    payload = {
        "produtos": [
            {
                "idProduto": product_id,
                "quantidade": 2
            }
        ]
    }
    
    

    response = requests.post(
        f"{BASE_URL}/carrinhos",
        headers=headers,
        json=payload
    )

    
    assert response.status_code == 201
    
    response = requests.delete(f"{BASE_URL}/carrinhos/concluir-compra", headers=headers)

    body = response.json()

    assert body["message"] == "Registro excluído com sucesso"
    
    response = requests.get(f"{BASE_URL}/produtos/{product_id}")
    assert response.status_code == 200

    stock_after = response.json()["quantidade"]

    assert stock_after == stock_before - 2
    
    
@pytest.mark.skip()
def test_buy_non_existent_cart(token_autentication):

    headers = {
        "Authorization": token_autentication
    }
    
    response = requests.delete(f"{BASE_URL}/carrinhos/concluir-compra", headers=headers)

    body = response.json()

    assert body["message"] == "Não foi encontrado carrinho para esse usuário"