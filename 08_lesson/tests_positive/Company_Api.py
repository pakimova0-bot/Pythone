import requests


class CompanyApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить список компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/api-v2/auth/companies',
                             params=params_to_add)
        return resp.json()

    # Получить токен авторизации
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=creds)
        return resp.json()["user_token"]

    # Добавить проект:
    def create_project(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/api-v2/projects',
                             json=company)
        return resp.json()
