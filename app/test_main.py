from fastapi.testclient import TestClient
from main import app

import os
os.environ["REDIS_URL"] = "redis://localhost"
client = TestClient(app)

def test_solution_completed():
    test_data = {
        "orders": [
            {
                "id": 1,
                "item": "Item 1",
                "quantity": 2,
                "price": 10.0,
                "status": "completed"
            },
            {
                "id": 2,
                "item": "Item 2",
                "quantity": 3,
                "price": 15.0,
                "status": "pending"
            }
        ],
        "criterion": "completed"
    }

    response = client.post("/solution", json=test_data)
    assert response.status_code == 200
    assert response.json() == 20.0 


def test_solution_all():

    test_data = {
        "orders": [
            {
                "id": 1,
                "item": "Item 1",
                "quantity": 2,
                "price": 10.0,
                "status": "completed"
            },
            {
                "id": 2,
                "item": "Item 2",
                "quantity": 3,
                "price": 15.0,
                "status": "pending"
            }
        ],
        "criterion": "all"
    }

    response = client.post("/solution", json=test_data)
    assert response.status_code == 200
    assert response.json() == 65.0

    '''
        
    '''