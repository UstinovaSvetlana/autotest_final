import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_chitai_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()


@allure.title("Поиск книг на кириллице")
@allure.description("Тест проверяет поиск книг на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_rus_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.rus_search('Алые паруса')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:46] == "Показываем результаты по запросу «алые паруса»"

@allure.title("Поиск книг на латинице")
@allure.description("Тест проверяет поиск книг на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_eng_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.rus_search('alye parusa')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:46] == "Показываем результаты по запросу ««alle parus»"

@allure.title("Пустое поле поиска")
@allure.description("Тест проверяет вылонение пустого поля поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_empty_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         main_page.empty_search("")
    with allure.step("Отсутствие действия на сайте"):
         url = browser.current_url
    assert url == "https://www.chitai-gorod.ru/"

@allure.title("Поиск по символам юникода")
@allure.description("Проверка поиска по символам юникода")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_search_invalid_ui():
    with allure.step("Открытие веб-страницы в Chrome, ввод символов юникода"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_invalid_ui('☯ ☭ ? $ £ ¢ ✉ § ©')
        assert text [0:28] == "Похоже, у нас такого нет"