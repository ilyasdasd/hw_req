import requests
from settings import TOKEN

class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'
    def __init__(self, token: str):
        self.token = token
        

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb' ), headers=self.get_headers())
        if response.status_code == 201:
            print('загрузка успешна') 


if __name__ == '__main__':
    ya = YaUploader(TOKEN)
    # Получить путь к загружаемому файлу и токен от пользователя
    ya.upload_to_disk('some_text.txt', '/new/se_text.txt')
