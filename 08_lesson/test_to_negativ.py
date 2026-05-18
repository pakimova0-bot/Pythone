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

    response = requests.post(f"{base_url}/api-v2/auth/keys/",  # не верный url
                             headers=headers, json=payload)

    assert response.status_code == 404


def test_to_change_empty_request_body():
    old = "Новое"
    new = "измененное"

    payload = {
        "title": old
        }

    response = requests.post(f"{base_url}projects",
                             headers=headers)

    assert response.status_code == 400
    response_bodi = response.json()
    id = response_bodi["id"]

# редактирование
    payload = {
        "title": new
        }

    response = requests.put(f"{base_url}projects/{id}",
                            headers=headers)  # без тела запроса

    assert response.status_code == 400

# получение по id

    response = requests.get(f"{base_url}projects/{id}",
                            headers=headers, json=payload)  # с телом запроса

    assert response.status_code == 400
    old = "Новое"
    new = "измененное"
