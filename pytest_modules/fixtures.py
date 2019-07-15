"""
pytest fixtures
"""
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox
from selenium.webdriver.chrome.options import Options as Chrome


@pytest.fixture(scope='function')
def start_browser(request):
    """
    Setup and run
    :param request: pytest request
    :param browser: name of browser that will start
    """
    browser = request.config.getoption("--browser")
    address = request.config.getoption("--address")
    if browser == "chrome":
        path = 'common/drivers/chromedriver'
        options = Chrome()
        options.headless = False
        driver = webdriver.Chrome(options=options, executable_path=path)
    elif browser == "firefox":
        path = 'common/drivers/geckodriver'
        options = Firefox()
        options.headless = False
        driver = webdriver.Firefox(options=options, executable_path=path)
    else:
        print('Bad wolf')
        sys.exit(1)
    driver.maximize_window()
    driver.get(address)
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver
