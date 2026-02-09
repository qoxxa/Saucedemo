import allure
from conftest import login_page
from data import TestData

data = TestData()

@allure.title("Авторизация")
@allure.description("Авторизация через стандартный логин")
@allure.id(1)
@allure.severity("Critical")
def test_standard_login(login_page):
    user = data.users.get("standard")
    actual_url = data.config.get("urls.products")
    title_page = data.messages.get("page_titles.products")

    login_page.login(user["login"])
    login_page.password(user["password"])
    login_page.login_button()

    check_transition = login_page.checking_title()

    assert login_page.driver.current_url == actual_url
    assert check_transition == title_page



@allure.title("Неверный пароль")
@allure.description("Авторизация с неверным паролем")
@allure.id(2)
@allure.severity("Critical")
def test_invalid_password(login_page):
    user = data.users.get("standard")
    password = data.users.get("invalid_passwords.invalid")
    actual_url = data.config.get("urls.base")
    error = data.messages.get("errors_login.invalid_password")

    login_page.login(user["login"])
    login_page.password(password)
    login_page.login_button()

    check_error = login_page.checking_error()

    assert login_page.driver.current_url == actual_url
    assert check_error == error

@allure.title("Заблокированный пользователь")
@allure.description("Авторизация заблокированного пользователя")
@allure.id(3)
@allure.severity("Critical")
def test_locked_username(login_page):
    user = data.users.get("locked_out")
    actual_url = data.config.get("urls.base")
    error = data.messages.get("errors_login.locked")

    login_page.login(user["login"])
    login_page.password(user["password"])
    login_page.login_button()

    check_error = login_page.checking_error()

    assert login_page.driver.current_url == actual_url
    assert check_error == error

@allure.title("Пустые поля ввода")
@allure.description("Авторизация с пустыми полями ввода")
@allure.id(4)
@allure.severity("Critical")
def test_empty_fields(login_page):
    actual_url = data.config.get("urls.base")
    error = data.messages.get("errors_login.empty_fields")

    login_page.login_button()
    check_error = login_page.checking_error()

    assert login_page.driver.current_url == actual_url
    assert check_error == error

@allure.title("Вход с задержкой")
@allure.description("Вход пользователя с задержкой интернета")
@allure.id(5)
@allure.severity("Critical")
def test_performance_glitch(login_page):
    user = data.users.get("performance_glitch")
    actual_url = data.config.get("urls.products")
    title_page = data.messages.get("page_titles.products")

    login_page.login(user["login"])
    login_page.password(user["password"])
    login_page.login_button()
    check_transition = login_page.checking_title()

    assert login_page.driver.current_url == actual_url
    assert check_transition == title_page
