from yandexDisk import YaUploader
import os

token = ""


def get_files_from_directory():
    # Если вводить вручную
    # path_to_directory = input('Введите путь директории')
    # Для быстрой отладки
    path_to_file = os.path.join(os.getcwd(), 'output_files')
    paths_to_files = []
    for file_name in os.listdir(path_to_file):
        paths_to_files.append(os.path.join(path_to_file, file_name))
    return paths_to_files


def upload_files_to_yandex_disk(paths):
    uploader = YaUploader(token)
    for file_paths in paths:
        uploader.upload(file_paths)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    files_paths: list = get_files_from_directory()
    upload_files_to_yandex_disk(files_paths)
