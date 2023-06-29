import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    request.cls.browser = browser
    yield browser
    browser.close()