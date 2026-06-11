#from urllib import response

import pytest
import requests
import time

email = f"renan{int(time.time())}@teste.com"
email_update = f"update{int(time.time())}@teste.com"
bearer_token = ""
id_usuario = ""
BASE_URL = "https://compassuol.serverest.dev"
produto_nome = f"mouse{int(time.time())}"

@pytest.fixture()
def setup_user():
    global id_usuario
    payload = {
        "nome": "teste da Silva",
        "email": email,
        "password": "teste",
        "administrador": "false"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 201
    body = response.json()
    id_usuario = body["_id"]


def test_list_users():
    response = requests.get(f"{BASE_URL}/usuarios")

    assert response.status_code == 200

    body = response.json()
    

    assert body["quantidade"] > 0

def test_return_fields():
    response = requests.get(f"{BASE_URL}/usuarios")

    assert response.status_code == 200

    body = response.json()
    

    assert body["quantidade"] > 0
    assert "nome" in body["usuarios"][0]
    assert "email" in body["usuarios"][0]
    assert "password" in body["usuarios"][0]
    assert "administrador" in body["usuarios"][0]
    assert "_id" in body["usuarios"][0]
    


def test_create_user():
    global id_usuario
    payload = {
        "nome": "teste da Silva",
        "email": email,
        "password": "teste",
        "administrador": "true"
        
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Cadastro realizado com sucesso"
    assert isinstance(body["_id"], str)
    id_usuario = body["_id"]


def test_create_user_with_duplicate_email():
    payload = {
        "nome": "teste da Silva",
        "email": email,
        "password": "teste",
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "Este email já está sendo usado"


def test_create_user_without_name():
    payload = {
        "email": email,
        "password": "teste",
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 400

    body = response.json()

    assert body["nome"] == "nome é obrigatório"


def test_create_user_with_empty_name():
    payload = {
        "nome": "",
        "email": email,
        "password": "teste",
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 400

    body = response.json()

    assert body["nome"] == "nome não pode ficar em branco"
    

def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/usuarios/{id_usuario}")

    assert response.status_code == 200

    body = response.json()

    
    assert body["nome"] == "teste da Silva"
    assert body["email"] == email
    assert body["password"] == "teste"
    assert body["administrador"] == "true"
    

    
def test_update_user():
    global id_usuario
    payload = {
        "nome": "atualizando teste da Silva",
        "email": email_update,
        "password": "teste1211111111111111111111111111111111111111",
        "administrador": "false"
    }
    
    

    response = requests.put(
        f"{BASE_URL}/usuarios/{id_usuario}",
        json=payload
    )
    

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Registro alterado com sucesso"


def test_delete_user():
    global id_usuario
    
    response = requests.delete(
        f"{BASE_URL}/usuarios/{id_usuario}"
    )
    

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Registro excluído com sucesso"


def test_login_sucess():
    global bearer_token
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Login realizado com sucesso"
    bearer_token = body["authorization"]


def test_create_product():
    global bearer_token

    headers = {
        "Authorization": bearer_token
    }
    
    payload = {
        "nome": produto_nome,
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    response = requests.post(
        f"{BASE_URL}/produtos",
        headers=headers,
        json=payload
    )

    assert response.status_code == 201
    
    body = response.json()
    
    assert body["message"] == "Cadastro realizado com sucesso"
    assert isinstance(body["_id"], str)

