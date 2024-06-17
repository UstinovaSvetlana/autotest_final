import requests
import allure
import pytest
import unittest

BASE_URL = "https://web-gate.chitai-gorod.ru/api/v1"
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwNjg5MzU0LCJpYXQiOjE3MTg2MTk2ODEsImV4cCI6MTcxODYyMzI4MSwidHlwZSI6MjB9.RCkmuAZXlXPE1ycTJkEUNFo-7mJ9ry5DT65XPbdy4gk"


@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"



@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_book_by_id():
    book_id = "alye-parusa-2505205"    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/products/slug/{book_id}", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Александр","Грин" in response.text
    
@allure.feature("API")
@allure.story("Поиск книг на кириллице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_rus_search_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=Алые паруса", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Алые паруса" in response.text

@allure.feature("API")
@allure.story("Поиск книг на латинице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_eng_search_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=alye parusa", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "alle parus" in response.text

@allure.feature("API")
@allure.story("Пустое поле")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_empty_search():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=", headers=headers)
    assert response.status_code == 400, f"Ожидался статус-код 400, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_space_search():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=   ", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"