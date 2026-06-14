cart_schema = {
    "type": "object",
    "required": [
        "produtos",
        "precoTotal",
        "quantidadeTotal",
        "idUsuario",
        "_id"
    ],
    "properties": {
        "produtos": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "idProduto",
                    "quantidade",
                    "precoUnitario"
                ],
                "properties": {
                    "idProduto": {
                        "type": "string",
                        "minLength": 1
                    },
                    "quantidade": {
                        "type": "integer",
                        "minimum": 1
                    },
                    "precoUnitario": {
                        "type": "integer",
                        "minimum": 0
                    }
                },
                "additionalProperties": False
            }
        },
        "precoTotal": {
            "type": "integer",
            "minimum": 0
        },
        "quantidadeTotal": {
            "type": "integer",
            "minimum": 1
        },
        "idUsuario": {
            "type": "string",
            "minLength": 1
        },
        "_id": {
            "type": "string",
            "minLength": 1
        }
    },
    "additionalProperties": False
}