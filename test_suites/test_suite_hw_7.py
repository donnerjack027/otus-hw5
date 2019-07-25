#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Test Suite - homework 7
"""

import pytest
import allure
from library.keywords import authorize_as_admin, add_new_product, \
    filter_products_by_name, delete_all_products, \
    add_new_product_with_images, delete_images_from_opencart, \
    demo_authorize, add_new_menu_field, add_file_to_opencart
from library.pages.product_page import ProductPage
from library.pages.main_page import MainPage
from library.constructor_menu import ConstructorMenu
from library.pages.downloads_page import DownloadsPage
from library.logger import web_logging
from common.sqllite.connection import main as proxy_logging


class TestSuiteHw6:
    """homework 7"""

    @staticmethod
    @allure.title('Critical: Add new product')
    @allure.severity("blocker")
    @pytest.mark.critical
    @pytest.mark.positive
    def test001(start_browser):
        """
        Test type - positive
        Add new product
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
        with allure.step('Authorize as admin'):
            authorize_as_admin(driver, login="admin", password="admin")
        with allure.step('Add new product'):
            add_new_product(driver,
                            product_name="Test product",
                            meta_tag="Test meta tag",
                            model="Test model")
        with allure.step('Creation check'):
            filter_products_by_name(driver, product_name="Test product")
            products = ProductPage.find_product_name(driver)
            for product in products:
                assert "Test product" in product.text
        with allure.step('Delete product'):
            delete_all_products(driver)
            ProductPage.accept_product_delete(driver)
        proxy_logging(proxy)
        # web_logging(driver)

    @staticmethod
    @allure.title('Critical: Delete product')
    @allure.severity("critical")
    @pytest.mark.critical
    @pytest.mark.positive
    def test002(start_browser):
        """
        Test type - positive
        Delete product
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
        with allure.step('Authorize as admin'):
            authorize_as_admin(driver, login="admin", password="admin")
        with allure.step('Add new product'):
            add_new_product(driver,
                            product_name="Test product",
                            meta_tag="Test meta tag",
                            model="Test model")
        with allure.step('Delete product'):
            filter_products_by_name(driver, product_name="Test product")
            delete_all_products(driver)
            ProductPage.accept_product_delete(driver)
        with allure.step('Deletion check'):
            filter_products_by_name(driver, product_name="Test product")
            products = ProductPage.find_product_name(driver)
            for product in products:
                assert "Test product" not in product.text
        proxy_logging(proxy)
        # web_logging(driver)

    @staticmethod
    @allure.title('High: Edit product')
    @allure.severity("normal")
    @pytest.mark.high
    @pytest.mark.positive
    def test003(start_browser):
        """
        Test type - positive
        Edit product
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
        with allure.step('Authorize as admin'):
            authorize_as_admin(driver, login="admin", password="admin")
        with allure.step('Add new product'):
            add_new_product(driver,
                            product_name="Test product",
                            meta_tag="Test meta tag",
                            model="Test model")
        with allure.step('Edit product'):
            filter_products_by_name(driver, product_name="Test product")
            ProductPage.find_and_click_edit_button(driver)
            ProductPage.clear_product_name_field(driver)
            ProductPage.input_product_name(driver, product_name="Edited test product")
            ProductPage.save_new_product_button_click(driver)
            ProductPage.clear_filter_name_filed(driver)
        with allure.step('Check product'):
            filter_products_by_name(driver, product_name="Edited test product")
            products = ProductPage.find_product_name(driver)
            for product in products:
                assert "Edited test product" in product.text
        with allure.step('Delete product'):
            filter_products_by_name(driver, product_name="Edited test product")
            delete_all_products(driver)
            ProductPage.accept_product_delete(driver)
        proxy_logging(proxy)
        # web_logging(driver)

    @staticmethod
    @allure.title('Medium: Create new product with 3 img')
    @allure.severity("normal")
    @pytest.mark.medium
    @pytest.mark.positive
    def test004(start_browser):
        """
        Test type - positive
        Create new product with 3 img
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
            images_names = ("1", "2", "3")
            jpg_names = list()
            for name in images_names:
                jpg_names.append(str(name)+".jpg")
        with allure.step('Authorize as admin'):
            authorize_as_admin(driver, login="admin", password="admin")
        with allure.step('Add new product with image'):
            add_new_product_with_images(driver,
                                        product_name="Test product",
                                        meta_tag="Test meta tag",
                                        model="Test model",
                                        images_path="/home/vasiliev_va/Downloads/special/",
                                        file_names=jpg_names)
        with allure.step('Check product'):
            ProductPage.check_images_names(driver, images_names)
        with allure.step('Delete image and product'):
            delete_images_from_opencart(driver, file_names=jpg_names)
            MainPage.open_product_catalog(driver)
            MainPage.click_product_button(driver)
            filter_products_by_name(driver, product_name="Test product")
            delete_all_products(driver)
            ProductPage.accept_product_delete(driver)
        proxy_logging(proxy)
        # web_logging(driver)

    @staticmethod
    @allure.title('Low: Add new menu field and drug and drop it')
    @allure.severity("minor")
    @pytest.mark.low
    @pytest.mark.skip(reason="Special for https://demo23.opencart.pro")
    @pytest.mark.positive
    def test005(start_browser):
        """
        Test type - positive
        add new menu field and drug and drop it
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
        with allure.step('Authorize as admin'):
            demo_authorize(driver, login="demo", password="demo")
        with allure.step('Add new menu field'):
            add_new_menu_field(driver)
        with allure.step('Check new menu field'):
            ConstructorMenu.check_computer_element(driver)
        proxy_logging(proxy)
        # web_logging(driver)

    @staticmethod
    @allure.title('Medium: Add new file to downloads menu')
    @allure.severity("normal")
    @pytest.mark.medium
    @pytest.mark.positive
    def test006(start_browser):
        """
        Test type - positive
        Add new file to downloads menu
        :param start_browser: browser run
        """
        with allure.step('Running test case'):
            driver, proxy = start_browser
            file_url = "/home/vasiliev_va/Downloads/special/1.jpg"
        with allure.step('Authorize as admin'):
            authorize_as_admin(driver, login="admin", password="admin")
        with allure.step('Add file to opencart'):
            add_file_to_opencart(driver, file_url, file_name="Test file")
        with allure.step('Check file'):
            DownloadsPage.select_downloaded_file(driver)
        with allure.step('Delete file'):
            DownloadsPage.delete_selected_file(driver)
        proxy_logging(proxy)
        # web_logging(driver)
