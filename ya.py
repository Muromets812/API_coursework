import requests


class YaUploader:
    def __init__(self, ya_token: str):
        self.ya_token = ya_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }

    def create_path(self, path_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_name}
        requests.put(url, headers=headers, params=params)
        return

    def upload_foto(self, url_dict, path_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': f"{path_name}/{url_dict['file_name']}.jpg", 'url': url_dict['url']}
        requests.post(url, headers=headers, params=params)
        return
