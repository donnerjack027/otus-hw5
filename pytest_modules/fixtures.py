"""
pytest fixtures
"""
import sys
from urllib.parse import urlparse
import pytest
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox
from selenium.webdriver.chrome.options import Options as Chrome
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from library.logger import OpencartListener

SERVER = Server(r"/home/vasiliev_va/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy")
SERVER.start()

PROXY = SERVER.create_proxy()
PROXY.new_har()


@pytest.fixture(scope='function')
def start_browser(request):
    """
    Setup and run
    :param request: pytest request
    """
    browser = request.config.getoption("--browser")
    address = request.config.getoption("--address")
    timeout = request.config.getoption("--timeout")
    url = urlparse(PROXY.proxy).path
    if browser == "chrome":
        des_cap = DesiredCapabilities.CHROME
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        path = 'common/drivers/chromedriver'
        options = Chrome()
        options.headless = False
        options.add_argument(argument='--proxy-server={0}'.format(url))
        # --- Without Grid --- #
        driver = EventFiringWebDriver(webdriver.Chrome(options=options,
                                                       executable_path=path,
                                                       desired_capabilities=des_cap),
                                      OpencartListener())
        # --- Locale Grid --- #
        # command_executor = 'http://192.168.102.28:4444/wd/hub'
        # driver = EventFiringWebDriver(webdriver.Remote(command_executor,
        #                                                desired_capabilities={"browserName": "chrome"}),
        #                               OpencartListener())
        # --- Remote Grid --- #
        # command_executor = 'http://donnerjack1:BTEizVzLqorX3SxBVyiB@hub.browserstack.com:80/wd/hub'
        # driver = EventFiringWebDriver(webdriver.Remote(command_executor,
        #                                                desired_capabilities={"browserName": "chrome",
        #                                                                      'os': 'Windows',
        #                                                                      'os_version': '10'}),
        #                               OpencartListener())
    elif browser == "firefox":
        des_cap = DesiredCapabilities.FIREFOX
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        path = 'common/drivers/geckodriver'
        options = Firefox()
        options.headless = False
        options.add_argument(argument='--proxy-server={0}'.format(url))
        # --- Without Grid --- #
        driver = EventFiringWebDriver(webdriver.Firefox(options=options,
                                                        executable_path=path),
                                      OpencartListener())
        # --- Locale Grid --- #
        # command_executor = 'http://192.168.102.28:4444/wd/hub'
        # driver = EventFiringWebDriver(webdriver.Remote(command_executor,
        #                                                desired_capabilities={"browserName": "firefox"}),
        #                               OpencartListener())
        # --- Remote Grid --- #
        # command_executor = 'http://donnerjack1:BTEizVzLqorX3SxBVyiB@hub.browserstack.com:80/wd/hub'
        # driver = EventFiringWebDriver(webdriver.Remote(command_executor,
        #                                                desired_capabilities={"browserName": "firefox",
        #                                                                      'os': 'Windows',
        #                                                                      'os_version': '10'}),
        #                               OpencartListener())
    else:
        print('Bad wolf')
        sys.exit(1)
    driver.maximize_window()
    driver.get(address)
    driver.implicitly_wait(int(timeout))
    request.addfinalizer(driver.quit)
    return driver, PROXY
