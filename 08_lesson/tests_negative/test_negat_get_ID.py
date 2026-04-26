import requests
import json


def test_get_ID():
    url = "https://ru.yougile.com/api-v2/projects/id"

    payload = json.dumps({
        "deleted": True,
        "id": "  ",
        "title": "ГосУслуги",
        "timestamp": 1623223299149,
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
            "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018":
            "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
        }
        })
    headers = {
        'Content-Type': 'application/json'
        }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 201
