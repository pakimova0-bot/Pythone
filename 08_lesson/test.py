def test_get_token():
    resp = requests.get("base_url+/api-v2/auth/keys/get")

    payload = json.dumps({
        "login": "p-akimova@mail.ru",
        "password": "inCanto720",
        "companyId": "10d06cee-fee2-4e80-9dc1-24192865b9dc"
    })
headers = {
        'Content-Type': 'application/json'
    }

response = requests.request("POST", resp, headers=headers, data=payload)
assert response.status_code == 201 

    # Список сотрудников
def test_list_of_employees():
        resp = requests.get("base_url+/api-v2/users")

        payload = json.dumps({
            "deleted": True,
            "id": "f2a19fb1-9e44-40cd-9009-35109fa470fe",
            "title": "ГосУслуги",
            "timestamp": 1623223299149,
            "apiData": "{}"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': '1YRlrg-QtbBoO5qGjbfCuGy0Y8W04MiZcnnbTRK3Xq0EsBZKsyXCz4pggyx26tPy'
        }

        response = requests.request("GET", resp, headers=headers, data=payload)

        assert response.status_code == 201 

        # список по Id
def test_get_ID():
    resp = requests.get("base_url+/api-v2/projects/id")

    payload = json.dumps({
        "deleted": True,
        "id": "42a2457d-b7ee-438a-9b90-b47e1aef17dc",
        "title": "ГосУслуги",
        "timestamp": 1768135957269,
        "users": {
            "b1800cde-b9d5-49f6-b8ef-04f86a422264": "admin"
        }
        })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'QtbBoO5qGjbfCuGy0Y8W04MiZcnnbTRK3Xq0EsBZKsyXCz4pggyx26tPy'
        }

response = requests.request("GET", resp, headers=headers, data=payload)

assert response.status_code == 201