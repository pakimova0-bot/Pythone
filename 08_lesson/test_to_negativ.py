import requests

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer'
        }
base_url = "https://ru.yougile.com/api-v2/"


def test_to_create_invalid_url():

    payload = {
        "title": "ГосУслуги"
        }

    response = requests.post(f"{base_url}upload-file",
                             headers=headers, json=payload)

    assert response.status_code == 201


def test_to_change_empty_request_body():
    old = "Новое"
    new = "измененное"

    payload = {
        "title": old
        }

    response = requests.post(f"{base_url}projects",
                             headers=headers, json=payload)

    assert response.status_code == 201
    response_bodi = response.json()
    id = ["id"]
# редактирование
    payload = {
        "title": new
        }

    response = requests.put(f"{base_url}projects/{id}",
                            headers=headers, json=payload)

    assert response.status_code == 200
# получение по id

    response = requests.delete(f"{base_url}projects/{id}", headers=headers)

    assert response.status_code == 200
    old = "Новое"
    new = "измененное"
