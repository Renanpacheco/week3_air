import pytest
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def generate_email():
    
    return f"renan{int(time.time() * 1000)}@teste.com"


@pytest.fixture
def register_user(generate_email):
    
    payload = {
        "nome": "teste da Silva",
        "email": generate_email,
        "password": "teste",
        "administrador": "true"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 201
    
    user_date = response.json()
    user_date["used_email"] = generate_email
    
    yield user_date
    
    requests.delete(f"{BASE_URL}/usuarios/{user_date['_id']}")



@pytest.fixture
def token_autentication():
    
    payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]



def test_list_users():
    response = requests.get(f"{BASE_URL}/usuarios")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0


def test_if_fields_are_present():
    response = requests.get(f"{BASE_URL}/usuarios")
    assert response.status_code == 200
    body = response.json()
    print(body)
    user = body["usuarios"][0]
    
    fields = ["nome", "email", "password", "administrador", "_id"]
    for field in fields:
        assert field in user


def test_create_user(generate_email):
    payload = {
        "nome": "teste da Silva",
        "email": generate_email,
        "password": "teste",
        "administrador": "true"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 201

    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert isinstance(body["_id"], str)


def test_create_user_with_duplicate_email(register_user):
    
    payload = {
        "nome": "teste da Silva",
        "email": register_user["used_email"],
        "password": "teste",
        "administrador": "false"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["message"] == "Este email já está sendo usado"


def test_create_user_without_name(generate_email):
    payload = {
        "email": generate_email,
        "password": "teste",
        "administrador": "false"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["nome"] == "nome é obrigatório"


def test_create_user_with_empty_name(generate_email):
    payload = {
        "nome": "",
        "email": generate_email,
        "password": "teste",
        "administrador": "false"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["nome"] == "nome não pode ficar em branco"
    

def test_get_user_by_id(register_user):
    
    id_user = register_user["_id"]
    
    response = requests.get(f"{BASE_URL}/usuarios/{id_user}")
    assert response.status_code == 200

    body = response.json()
    assert body["nome"] == "teste da Silva"
    assert body["email"] == register_user["used_email"]
    assert body["password"] == "teste"
    assert body["administrador"] == "true"
    

def test_update_user(register_user):
    id_user = register_user["_id"]
    email_update = f"update{int(time.time() * 1000)}@teste.com"
    
    payload = {
        "nome": "atualizando teste da Silva",
        "email": email_update,
        "password": "teste1211111111111111111111111111111111111111",
        "administrador": "false"
    }

    response = requests.put(f"{BASE_URL}/usuarios/{id_user}", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert body["message"] == "Registro alterado com sucesso"


def test_delete_user(register_user):
    
    id_user = register_user["_id"]
    
    response = requests.delete(f"{BASE_URL}/usuarios/{id_user}")
    assert response.status_code == 200

    body = response.json()
    assert body["message"] == "Registro excluído com sucesso"