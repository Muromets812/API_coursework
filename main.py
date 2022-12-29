from pprint import pprint
from tqdm import tqdm
from vk import VK
from ya import YaUploader

ACCESS_TOKEN = ''

if __name__ == '__main__':
    YA_TOKEN = input("Введите токен доступа на ya.disk: ")
    while True:
        key = input("Для продолженя работы с программой введите 'start', для выхода 'exit': ")
        if key == 'start':
            user_id = input("Введите id пользователя VK: ")
            path_name = input("Введите имя папки на ya.disk куда будут загружены фото: ")
            vk = VK(ACCESS_TOKEN, user_id)
            vk._json_create()
            ya = YaUploader(YA_TOKEN)
            ya.create_path(path_name)
            mylist = vk._create_foto_list()
            pbar = tqdm()
            pbar.reset(total=len(mylist))
            for item in mylist:
                ya.upload_foto(url_dict=item, path_name=path_name)
                pbar.update()
            pbar.close()
        else:
            break
