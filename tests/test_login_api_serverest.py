import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

'''
* Login com senha inválida.
* Login sem informar email.
* Login sem informar senha.
'''

@pytest.mark.skip()
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

def test_login_wrong_email():
    payload = {
        "email": "inexistente13141414515555555555551241541451512@qa.com",
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 401

    body = response.json()
    assert body["message"] == "Email e/ou senha inválidos"

def test_login_wrong_password():
    payload = {
        "email": "fulano@qa.com",
        "password": "teste13244144124124124"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 401

    body = response.json()
    assert body["message"] == "Email e/ou senha inválidos"

def test_login_without_email():
    payload = {
        "password": "teste"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["email"] == "email é obrigatório"

def test_login_without_password():
    payload = {
        "email": "fulano@qa.com"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400

    body = response.json()
    assert body["password"] == "password é obrigatório"