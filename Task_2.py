import requests
import pathlib

class YaUploader:
    token = 'AQAAAAAgNguaAADLW-kIgkiY_U5erHKy8MLG8kk'
    def __init__(self, file_path):
        self.file_path = file_path
    def upload(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': self.file_path.name,
                  'overwrite': 'true'}
        upload_link = requests.get(url, headers=headers, params=params).json()['href']
        res = requests.put(upload_link, data=open(self.file_path, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            return 'Файл успешно загружен на Я.Диск'
        return 'Ошибка загрузки'

if __name__ == "__main__":

    uploader = YaUploader(pathlib.Path('Task_2.txt'))
    print(uploader.upload())