#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
product page
"""

from library.locators import Locators
from library.base_page import BasePage


class ProductPage(BasePage):
    """
    Product page methods
    """
    @staticmethod
    def add_new_product_button_click(driver):
        """
        Click on add new product button
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.add_new_product_locator)

    @staticmethod
    def clear_product_name_field(driver):
        """
        Clear the product name field
        :param driver: browser web driver
        """
        BasePage.clear_object(driver, locator=Locators.name_input_field_locator)

    @staticmethod
    def input_product_name(driver, product_name):
        """
        Input product name in add new product menu
        :param driver: browser web driver
        :param product_name: name of the product that we want to add
        """
        BasePage.send_keys(driver,
                           locator=Locators.name_input_field_locator,
                           some_keys=product_name)

    @staticmethod
    def input_meta_tag(driver, meta_tag):
        """
        Input meta tag for new product
        :param driver: browser web driver
        :param meta_tag: meta tag of product that we want to add
        """
        BasePage.send_keys(driver, locator=Locators.meta_title_locator, some_keys=meta_tag)

    @staticmethod
    def data_tab_click(driver):
        """
        Click on data tag for new product
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.data_tab_locator)

    @staticmethod
    def input_model(driver, model):
        """
        Input model to the model field for product that we want to add
        :param driver: browser web driver
        :param model: model of the new product
        """
        BasePage.send_keys(driver, locator=Locators.model_input_field_locator, some_keys=model)

    @staticmethod
    def save_new_product_button_click(driver):
        """
        Click on save new product button
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.save_new_product_button_locator)

    @staticmethod
    def clear_filter_name_filed(driver):
        """
        Clear product filter name field
        :param driver: browser web driver
        """
        BasePage.clear_object(driver, locator=Locators.product_name_filter_locator)

    @staticmethod
    def input_product_name_to_filter(driver, product_name):
        """
        Enter product name to the product filter
        :param driver: browser web driver
        :param product_name: product name by that we will filter products
        """
        BasePage.send_keys(driver,
                           locator=Locators.product_name_filter_locator,
                           some_keys=product_name)

    @staticmethod
    def click_filter_button(driver):
        """
        Click on filter assert button
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.filter_button_locator)

    @staticmethod
    def find_product_name(driver):
        """
        Find product name from the product list
        :param driver: browser web driver
        :return product
        """
        products = driver.find_elements(*Locators.product_form_locator)
        return products

    @staticmethod
    def click_choose_all_products_checkbox(driver):
        """
        Iter all checkboxes and found checkbox for choose all products
        :param driver: browser web driver
        """
        BasePage.click_on_first_object_from_many(driver,
                                                 locator=Locators.checkboxes_locator,
                                                 attribute='type',
                                                 attribute_value='checkbox')

    @staticmethod
    def click_delete_all_products_button(driver):
        """
        Delete all choosed products
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.delete_products_locator)

    @staticmethod
    def accept_product_delete(driver):
        """
        Accept project delete message
        :param driver: browser web driver
        """
        BasePage.alert_accept_click(driver)

    @staticmethod
    def find_and_click_edit_button(driver):
        """
        Find from buttons edit button and click it
        :param driver: browser web river
        """
        BasePage.click_on_first_object_from_many(driver,
                                                 locator=Locators.edit_product_button_locator,
                                                 attribute='data-original-title',
                                                 attribute_value='Edit')
