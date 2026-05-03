import requests
import json

def test_simpl():
    url = "https://ru.yougile.com/api-v2/projects"

    payload = json.dumps({
    "title": "/api-v2/projects"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1YRlrg-QtbBoO5qGjbfCuGy0Y8W04MiZcnnbTRK3Xq0EsBZKsyXCz4pggyx26tPy'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 201 