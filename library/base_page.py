#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
base methods
"""

from library.locators import Locators


def input_login(driver, login):
    """
    Input email address to login field
    :param driver: browser web driver
    :param login: user email address
    """
    locator = Locators.email_input_locator
    driver.find_element(*locator).send_keys(login)


def input_password(driver, password):
    """
    Input password to password field
    :param driver: browser web driver
    :param password: user password
    """
    locator = Locators.password_input_locator
    driver.find_element(*locator).send_keys(password)


def accept_click(driver):
    """
    Click on accept button
    :param driver: browser web driver
    """
    locator = Locators.login_button_locator
    driver.find_element(*locator).click()


def get_warning_message(driver):
    """
    Parse warning object to get warning text
    :param driver: browser web driver
    :return: text - error message
    """
    locator = Locators.warning_locator
    response = driver.find_element(*locator)
    error_text = response.text
    return error_text
