import requests
from yandexDisk import YaUploader
import os
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_file = input()
    # Для быстрой отладки
    path_to_file = os.path.join(os.getcwd(), '1.txt')
    token = "y0_AgAAAAAIX_RZAADLWwAAAADMy68nbBBNWYDHRl6DGrNSZa6PJvVBTb0"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)