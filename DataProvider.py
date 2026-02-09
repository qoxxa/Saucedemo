# import json
# import os
#
# # Получаем путь к директории, где находится этот файл
# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, 'test_data.json')
#
# # Открываем и загружаем JSON
# with open(file_path, 'r', encoding='utf-8') as my_file:
#     global_data = json.load(my_file)
#
#
# class DataProvider:
#     def __init__(self) -> None:
#         self.data = global_data
#
#     def get(self, key: str) -> str:
#         """Возвращает значение по ключу как строку"""
#         keys = key.split(".")
#         value = self.data
#         for k in keys:
#             value = value[k]
#         return value
#
#     def getint(self, prop: str) -> int:
#         """Возвращает значение по ключу как целое число"""
#         val = self.data.get(prop)
#         if val is None:
#             raise ValueError(f"Ключ '{prop}' не найден в test_data.json")
#         try:
#             return int(val)
#         except (ValueError, TypeError):
#             raise ValueError(f"Значение '{val}' для ключа '{prop}' нельзя преобразовать в int")
import json
import os

# Определяем корень проекта (где лежит conftest.py или pytest.ini)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

class DataProvider:
    def __init__(self, filename: str):
        # Ищем файл в папке test_data/
        file_path = os.path.join(PROJECT_ROOT, "test_data", filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get(self, key: str):
        keys = key.split(".")
        value = self.data
        for k in keys:
            value = value[k]
        return value