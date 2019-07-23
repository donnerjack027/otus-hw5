#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
product page
"""

import os
import logging as log
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from library.locators import Locators
from library.base_page import BasePage
from library.waiters import wait_for_element, wait_for_alert


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

    @staticmethod
    def click_on_image_tab(driver):
        """
        Click on image tab in create new product menu
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.image_tab_button_locator)

    @staticmethod
    def click_on_image(driver):
        """
        Click on image in create new product menu
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.product_image_locator)

    @staticmethod
    def click_on_edit_image_button(driver):
        """
        Click on image edit button in new product menu
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.image_edit_button_locator)

    @staticmethod
    def add_new_images_to_store(driver, images_path, *file_names):
        """
        Add images to the opencart store
        :param driver: browser web driver
        :param images_path: path to images tuple
        :param file_names: names of images we wanna to load
        """
        dirname = os.path.dirname(images_path)
        for arg in file_names:
            filename = os.path.join(str(dirname), str(arg))
            wait_for_element(driver, Locators.image_download_button_locator, delay=3)
            driver.find_element(*Locators.image_download_button_locator).click()
            keyboard = Controller()
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            driver.find_element(*Locators.image_download_dynamic_locator).send_keys(filename)
            alert_message = "Success: Your file has been uploaded!"
            wait_for_alert(driver, alert_message, delay=3)
            BasePage.alert_accept_click(driver)

    @staticmethod
    def close_add_image_menu():
        """
        Close menu for import images in new product menu
        """
        mouse = MouseController()
        mouse.press(Button.left)
        mouse.release(Button.left)

    @staticmethod
    def click_on_add_image_button(driver):
        """
        Click on add new image button in new product menu
        :param driver: browser web driver
        """
        BasePage.click_on_first_object_from_many(driver,
                                                 locator=Locators.add_image_locator,
                                                 attribute="data-original-title",
                                                 attribute_value="Add Image")

    @staticmethod
    def add_images_to_product(driver, *file_names):
        """
        Add images to product from opencart store
        :param driver: browser web driver
        :param file_names: names of images that we loaded before it
        """

        if len(file_names) == 1:
            ProductPage.click_on_image(driver)
            ProductPage.click_on_edit_image_button(driver)
            BasePage.click_on_object(
                driver,
                locator=(By.XPATH, '//*[@title="%s"]', str(file_names)))
            ProductPage.close_add_image_menu()
        if len(file_names) > 1:
            ProductPage.click_on_image(driver)
            ProductPage.click_on_edit_image_button(driver)
            BasePage.click_on_object(
                driver,
                locator=(By.XPATH, '//*[@title="%s"]', str(file_names[0])))
            ProductPage.close_add_image_menu()
            thumb_image_number = 0
            for name in range(1, len(file_names)):
                ProductPage.click_on_add_image_button(driver)
                BasePage.click_on_object(
                    driver,
                    locator=(By.ID, 'thumb-image%s', thumb_image_number))
                thumb_image_number += 1
                ProductPage.click_on_edit_image_button(driver)
                BasePage.click_on_object(
                    driver,
                    locator=(By.XPATH, '//*[@title="%s"]', str(file_names[name])))
        else:
            log.error('Number of file names out of >= 1 - %s', file_names)

    @staticmethod
    def check_images_names(driver, images_names):
        """
        Check that images with names in 'image_names' are used in product
        :param driver: browser web driver
        :param images_names: list of images names
        """
        opencart_url = "'http://192.168.110.60/opencart/image/cache/catalog/"
        for image in images_names:
            image_xpath = "//img[@src=" + opencart_url + image + "-100x100.jpg']"
            wait_for_element(driver, (By.XPATH, image_xpath))
            driver.find_element(By.XPATH, image_xpath)
        log.info("All elements has been found")

    @staticmethod
    def choose_remove_images_by_names(driver, file_names):
        """
        Delete all images by names
        :param driver: browser web driver
        :param file_names: names of images that we wanna delete
        """
        for arg in file_names:
            BasePage.click_on_all_object_from_many(driver,
                                                   locator=Locators.checkboxes_locator,
                                                   attribute="value",
                                                   attribute_value="catalog/{}".format(arg))

    @staticmethod
    def delete_selected_images(driver):
        """
        Delete selected images from opencart
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=Locators.delete_images_button_locator)
        wait_for_alert(driver, alert_message="Are you sure?", delay=2)
        BasePage.alert_accept_click(driver)
        wait_for_alert(driver, alert_message="Success: Your file or directory has been deleted!")
        BasePage.alert_accept_click(driver)
