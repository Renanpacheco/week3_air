import pytest
import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def test_list_carts():
    response = requests.get(f"{BASE_URL}/carrinhos")
    assert response.status_code == 200
    body = response.json()
    assert body["quantidade"] > 0