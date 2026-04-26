import requests
import json


base_url = "https://ru.yougile.com"


def test_to_change():

    resp = requests.get(base_url+'/api-v2/projects/{id}')
    response_body = resp.json()

    payload = json.dumps({
        "deleted": True,
        "title": "ГосУслуги",
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
            "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018":
            "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
        }
    })
    headers = {
        'id': '4f6f0391-0f94-4d30-9b0e-99430a36d4fb',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", base_url, headers=headers, data=payload)

    assert response.status_code == 200
