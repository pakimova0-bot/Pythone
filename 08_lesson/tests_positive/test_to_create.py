import requests
import json


def test_to_create():
    url = "https://ru.yougile.com/api-v2/projects"

    payload = json.dumps({
        "title": "ГосУслуги"
        })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 3p3pq-'
        'pzoQb03hAIbZ3zGBqHQtQkKeORQY4VWKTCPEnQ-wmyHkrZxpfiuYHeZbMr'
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 201
