import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()


    with allure.step("Политика куки"):
        def set_cookie_policy(self): 
            cookie = {"name": "cookie_policy", "value": "1"}
            self._driver.add_cookie(cookie)


    with allure.step("Поиск книг на кириллице"):
        def rus_search(self,term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt
           
    with allure.step("Поиск книг на латинице"):
        def eng_search(self,term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

    with allure.step("Пустое поле поиска"):
        def empty_search(self,term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()

    with allure.step("Поиск по символам юникода"):
        def search_invalid_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.CLASS_NAME, "catalog-empty-result__description").text
            return txt

        