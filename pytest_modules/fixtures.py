"""
pytest fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox
from selenium.webdriver.chrome.options import Options as chrome


@pytest.fixture
def start_browser(request):
    """
    Setup and run browser
    :param request: pytest request
    :param browser: name of browser that will start
    """
    browser = request.config.getoption("--browser")
    chromedriver_path = 'common/drivers/chromedriver'
    firefoxdriver_path = 'common/drivers/geckodriver'
    if browser == "chrome":
        options = chrome()
        options.headless = True
        wd = webdriver.Chrome(options=options, executable_path=chromedriver_path)
    else:
        options = firefox()
        options.headless = True
        wd = webdriver.Firefox(options=options, executable_path=firefoxdriver_path)
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def open_login_page(request, start_browser):
    """
    Opencart start page
    """
    url = 'opencart/index.php?route=account/login'
    parametrized_url = request.config.getoption("--address")
    opencart_address = str(parametrized_url)+str(url)
    return opencart_address
