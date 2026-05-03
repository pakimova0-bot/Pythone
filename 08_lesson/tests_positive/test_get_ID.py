import requests
import json


def test_compani():
    resp = requests.post('https://ru.yougile.com/api-v2/auth/companies')

    payload = json.dumps({
        "login": "p-akimova@mail.ru",
        "password": "inCanto720"
        })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", resp, headers=headers, data=payload)

    print(response.text)
