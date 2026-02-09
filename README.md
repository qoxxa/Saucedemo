# Проект: Автоматизированные тесты saucedemo.com

# Задача

Данный проект предназначен для автоматизации тестирования веб-сайта saucedemo.com. Тесты охватывают различные проверки аутентификации пользователя, работу с товарами и корзиной сайта.

## Запуск тестов

Для запуска тестов выполните следующие шаги:
1. Склонировать проект

2. Убедитесь, что у вас установлены все зависимости, указанные в файле `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите тесты с генерацией отчётности
      ```bash
     pytest -s -v --alluredir=allure-results tests
     ```

   и откройте отчёт с помощью команды:
   ```
    allure serve allure-results
   ```
   
4. Для автоматизации отчётности allure, используйте скрипт `run.sh` командой
   ```bash
   ./run.sh
   ```

5. Сборка и запуск в Dockers:
- Собрать dockers образ
    ```bash
   docker build -t saucedemo-tests .
    ```
- Запустить тесты
    ```bash
   docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-tests
    ```
- Сгенерировать отчёт с помощью команды:
    ```
   allure serve allure-results
    ```

## Структура проекта
```
Saucedemo/
│
├── 📂 pages
│ ├── 📄 cart_page # Методы для работы со страницей корзины
│ ├── 📄 login_page # Методы для работы со страницей входа
│ ├── 📄 product_page # Методы для работы со страницей товаров
├── 📂 test_data
│ ├── 📄 config.json # browsers, urls, env
│ ├── 📄 messages.json # ошибки, заголовки, тексты
│ ├── 📄 products.json # товары, цены, ID
│ ├── 📄 selectors.json # все селекторы
│ ├── 📄 sort.json # опции сортировки
│ ├── 📄 users.json # valid & invalid credentials
├── 📂 tests
│ ├── 📄 test_cart.py # UI автотесты корзины
│ └── 📄 test_login.py # UI автотесты логина
│ └── 📄 test_product.py # UI автотесты товаров
│
├── 📄 data.py # Методы для работы с тестовыми данными
├── 📄 requirements.txt # Зависимости Python
├── 📄 pytest.ini # Конфигурация pytest
├── 📄 run.sh # Скрипт запуска тестов и генерации отчета
├── 📄 Dockerfile  # Файл конфигурации Doker
├── 📄 DataProvider.py # Утилита для получения данных из test_data.json
└── 📄 conftest.py # Фикстуры и настройки Pytest
```