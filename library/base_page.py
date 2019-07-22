#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
base page
"""
from library.waiters import wait_for_element


class BasePage:
    """
    Base page methods
    """
    @staticmethod
    def send_keys(driver, locator, some_keys):
        """
        Send keys to the object
        :param locator: object locator
        :param driver: browser web driver
        :param some_keys: keys we want to send
        """
        wait_for_element(driver, locator)
        driver.find_element(*locator).send_keys(some_keys)

    @staticmethod
    def click_on_object(driver, locator):
        """
        Click on object by locator
        :param driver: browser web driver
        :param locator: object locator
        """
        wait_for_element(driver, locator)
        driver.find_element(*locator).click()

    @staticmethod
    def click_on_first_object_from_many(driver, locator, attribute, attribute_value):
        """
        Find and click on object from many objects by it attribute value
        :param driver: browser web driver
        :param locator: object locator
        :param attribute: object attribute
        :param attribute_value: object attribute value
        """
        wait_for_element(driver, locator)
        buttons = driver.find_elements(*locator)
        for button in buttons:
            data = button.get_attribute(str(attribute))
            if data == attribute_value:
                button.click()
                break
            else:
                continue

    @staticmethod
    def alert_accept_click(driver):
        """
        Click accept on message
        :param driver: browser web driver
        """
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

    @staticmethod
    def clear_object(driver, locator):
        """
        Clear and object field
        :param driver: browser web driver
        :param locator: object locator
        """
        wait_for_element(driver, locator)
        driver.find_element(*locator).clear()
