import os
import pytest

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Загрузки/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://yandex.ru/")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    _driver = None
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        _driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        _driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)
    elif browser == "opera":
        _driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")

    _driver.maximize_window()

    _driver.base_url = base_url
    yield _driver

    _driver.quit()
