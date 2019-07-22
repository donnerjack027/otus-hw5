#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
waiters
"""

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def wait_for_element(driver, locator, delay=5):
    """
    Waiting for element visible by locator
    :param driver: browser driver
    :param locator: locator of element
    :param delay: max time
    """
    try:
        WebDriverWait(driver, int(delay)).until(EC.presence_of_element_located(locator))
    except(NoSuchElementException, TimeoutException):
        driver.save_screenshot("./wait_for_element_screenshot.png")
        logging.error("There are no visible element in delay %s", delay)
