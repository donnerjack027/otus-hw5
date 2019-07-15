#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Test Suite - homework 6
"""

import logging
import pytest
from library.base_page import input_login, input_password, get_warning_message, accept_click


class TestSuiteHw6:
    """homework 6 - positive and negative test case for login window"""

    @staticmethod
    @pytest.mark.positive
    def test_login_success(start_browser):
        """
        Login with valid parameters.
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="support@localhost.ru")
        input_password(driver, password="support")
        accept_click(driver)
        success_login_url = 'http://192.168.110.60/opencart/index.php?route=account/account'
        logging.debug("Current web url is %s", driver.current_url)
        assert driver.current_url == success_login_url

    @staticmethod
    @pytest.mark.positive
    def test_login_success__email_in_uppercase(start_browser):
        """
        Login with valid parameters. E-Mail Address in uppercase.
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="SUPPORT@LOCALHOST.ru")
        input_password(driver, password="support")
        accept_click(driver)
        current_url = driver.current_url
        success_login_url = 'http://192.168.110.60/opencart/index.php?route=account/account'
        logging.debug("Current web url is %s", driver.current_url)
        assert current_url == success_login_url

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__password_in_uppercase(start_browser):
        """
        Login with valid parameters. Password in uppercase.
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="support@localhost.ru")
        input_password(driver, password="SUPPORT")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: No match for E-Mail Address and/or Password."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__invalid_email(start_browser):
        """
        Login with invalid E-Mail Address
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="opencart22@localhost.ru")
        input_password(driver, password="support")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: No match for E-Mail Address and/or Password."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__invalid_password(start_browser):
        """
        Login with invalid password
        :param start_browser:  browser run
        """
        driver = start_browser
        input_login(driver, login="support@localhost.ru")
        input_password(driver, password="wrongpassword")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: No match for E-Mail Address and/or Password."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__invalid_password_and_email(start_browser):
        """
        Login with invalid password and E-Mail Address
        :param start_browser:  browser run
        """
        driver = start_browser
        input_login(driver, login="support@wronglogin.ru")
        input_password(driver, password="wrongpassword")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: No match for E-Mail Address and/or Password."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text

    @staticmethod
    @pytest.mark.positive
    def test_login_success__numbers_in_login(start_browser):
        """
        Login with valid parameters. Have numbers in login
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="1111@1111.ru")
        input_password(driver, password="support")
        accept_click(driver)
        success_login_url = 'http://192.168.110.60/opencart/index.php?route=account/account'
        logging.debug("Current web url is %s", driver.current_url)
        assert driver.current_url == success_login_url

    @staticmethod
    @pytest.mark.positive
    def test_login_success__numbers_in_password(start_browser):
        """
        Login with valid parameters. Have numbers in password
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="support2@localhost.ru")
        input_password(driver, password="1111111")
        accept_click(driver)
        success_login_url = 'http://192.168.110.60/opencart/index.php?route=account/account'
        logging.debug("Current web url is %s", driver.current_url)
        assert driver.current_url == success_login_url

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__without_email(start_browser):
        """
        Login with NONE E-Mail Address
        :param start_browser: browser run
        """
        driver = start_browser
        input_password(driver, password="123456")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: Your account has exceeded allowed " \
                        "number of login attempts. Please try again in 1 hour."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text

    @staticmethod
    @pytest.mark.negative
    def test_login_not_success__without_password(start_browser):
        """
        Login with NONE password
        :param start_browser: browser run
        """
        driver = start_browser
        input_login(driver, login="support@localhost.ru")
        accept_click(driver)
        error_text = get_warning_message(driver)
        correct_error = "Warning: No match for E-Mail Address and/or Password."
        logging.debug("Current web url is %s", driver.current_url)
        logging.debug("Error text is %s", error_text)
        assert correct_error == error_text
