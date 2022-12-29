import json
import requests


class VK:
    URL = 'https://api.vk.com/method/'

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def _get_foto(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'extended': 1, 'count': 5, 'rev': 0, 'photo_sizes': 1}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def _create_foto_list(self):
        raw_dict = self._get_foto()
        rlist = []
        for item in raw_dict['response']['items']:
            rlist.append({'file_name': item['likes']['count'], 'url': item['sizes'][-1]['url']})
        return rlist

    def _json_create(self):
        rlist = []
        raw_dict = self._get_foto()
        for item in raw_dict['response']['items']:
            rlist.append({'file_name': f"{item['likes']['count']}.jpg", 'size': item['sizes'][-1]['type']})
        with open('info_foto.json', "w") as f:
            json.dump(rlist, f, ensure_ascii=False, indent=2)
        return
