import requests

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 3p3pq-'
        'pzoQb03hAIbZ3zGBqHQtQkKeORQY4VWKTCPEnQ-wmyHkrZxpfiuYHeZbMr'
        }
base_url = "https://ru.yougile.com/api-v2/"


def test_to_create():

    payload = {
        "title": "????"
        }

    response = requests.post(f"{base_url}projects",
                             headers=headers, json=payload)

    assert response.status_code == 201


def test_to_change():
    old = "Новое"
    new = "измененное"

    payload = {
        "title": old
        }

    response = requests.post(f"{base_url}project",
                             headers=headers, json=payload)

    assert response.status_code == 201
    response_bodi = response.json()
    id = response_bodi["id"]
# редактирование
    payload = {
        "title": new
        }

    response = requests.put(f"{base_url}projects/{id}",
                            headers=headers, json=payload)

    assert response.status_code == 200
# получение по id

    response = requests.get(f"{base_url}projects/{id}", headers=headers)

    assert response.status_code == 400
    old = "Новое"
    new = "измененное"
