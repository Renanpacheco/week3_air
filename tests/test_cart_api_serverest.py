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