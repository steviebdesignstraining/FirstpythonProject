import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
# (params=["chrome", "firefox"]) # Chrome driver is set here so that it's not repeated and can be called like a beforeEach hook
def driver(request):
    # Run scripts either on chrome or firefox
    browser = request.config.getoption("--browser")
    # Run scripts via parallel
    # browser = request.param
    # f = format
    print(f'Creating {browser} driver')
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute test (chrome or firefox)"
    )


class NoSuchElementException(WebDriverException):
    def pytest_addoption(self):