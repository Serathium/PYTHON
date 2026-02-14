import json

products_json = '''
[
    {
        "id": "PROD-001",
        "name": "Wireless Mouse",
        "price": 24.99,
        "in_stock": true
    },
    {
        "id": "PROD-002",
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "in_stock": false
    },
    {
        "id": "PROD-003",
        "name": "USB-C Hub",
        "price": 34.99,
        "in_stock": true
    }
]
'''

products = json.loads(products_json)


id = [i["id" ] for i in products]

print(f"{id}")