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
        driver.save_screenshot('./wait_for_element_screenshot.png')
        logging.error('There are no visible element in delay %s', delay)


def wait_for_alert(driver, alert_message, delay=5):
    """
    Waiting for alert
    :param driver: browser web driver
    :param alert_message: message in the alert window
    :param delay: maximal time that we waiting alert
    """
    try:
        WebDriverWait(driver, int(delay)).until(EC.alert_is_present(), alert_message)
    except(NoSuchElementException, TimeoutException):
        driver.save_screenshot("./alert_screenshot.png")
        logging.error('There are alert with message:%s', alert_message)
