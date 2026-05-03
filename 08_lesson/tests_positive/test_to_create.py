import requests
import json


def create_project():
    url = "https://ru.yougile.com/api-v2/projects"

    payload = json.dumps({
        "title": "ГосУслуги",
        "users": {
            "users": "admin"
            }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 201
