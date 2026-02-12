import pytest
import requests
import json

def load_users():
    with open('users.json', 'r') as f:
        return json.load(f)
    
@pytest.mark.parametrize("username", load_users())
def test_post_user_data(username):
    # API URL (Endpoint)
    url = "https://jsonplaceholder.typicode.com/posts"

    # Requisition body (Payload)
    payload = {
        "title": "Automation test",
        "body": f"Validating the user {username}",
        "userId": 1
    }

    # 1. POST requisition (send data)
    response = requests.post(url, json=payload)

    # 2. Validations (Assertations)
    # Status 201 means "Created" (Success in creation)
    assert response.status_code == 201
    
    # Converts the response to JSON and validates the content
    data = response.json()
    assert data["body"] == f"Validating the user {username}"
    assert "id" in data  # Makes sure the server generated an ID