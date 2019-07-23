#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
main page
"""

from library.locators import Locators
from library.base_page import BasePage


class MainPage(BasePage):
    """
    Main page methods
    """
    @staticmethod
    def message_close_button_click(driver):
        """
        Click on close button of the message
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.message_close_button_locator)

    @staticmethod
    def open_product_catalog(driver):
        """
        Open product catalog combobox
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.product_catalog_locator)

    @staticmethod
    def click_product_button(driver):
        """
        Click on product button in the catalog
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.product_button_locator)

    @staticmethod
    def click_design_menu(driver):
        """
        Open design menu combobox
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.design_menu_locator)

    @staticmethod
    def click_menu_constructor(driver):
        """
        Click on menu constructor in main menu
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.menu_constructor_locator)
