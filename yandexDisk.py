import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}',
        }


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        host = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        params = {"path": file_path.split('\\')[-1], "owerwrite": "true"}
        headers = self.get_headers()
        response = requests.get(host, headers=headers, params=params)
        href = response.json().get('href')
        response = requests.put(href, data=open(file_path, 'rb'))
