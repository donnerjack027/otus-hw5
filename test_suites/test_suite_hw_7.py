#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Test Suite - homework 7
"""

import pytest
from library.keywords import authorize_as_admin, add_new_product, \
    filter_products_by_name, delete_all_products, \
    add_new_product_with_images, delete_images_from_opencart, \
    demo_authorize, add_new_menu_field
from library.pages.product_page import ProductPage
from library.pages.main_page import MainPage
from library.constructor_menu import ConstructorMenu


class TestSuiteHw6:
    """homework 7"""

    @staticmethod
    @pytest.mark.positive
    def test001(start_browser):
        """
        Test type - positive
        Add new product
        :param start_browser: browser run
        """
        driver = start_browser

        authorize_as_admin(driver, login="admin", password="admin")
        add_new_product(driver,
                        product_name="Test product",
                        meta_tag="Test meta tag",
                        model="Test model")
        filter_products_by_name(driver, product_name="Test product")
        products = ProductPage.find_product_name(driver)
        for product in products:
            assert "Test product" in product.text
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)

    @staticmethod
    @pytest.mark.positive
    def test002(start_browser):
        """
        Test type - positive
        Delete product
        :param start_browser: browser run
        """
        driver = start_browser
        authorize_as_admin(driver, login="admin", password="admin")
        add_new_product(driver,
                        product_name="Test product",
                        meta_tag="Test meta tag",
                        model="Test model")
        filter_products_by_name(driver, product_name="Test product")
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)
        filter_products_by_name(driver, product_name="Test product")
        products = ProductPage.find_product_name(driver)
        for product in products:
            assert "Test product" not in product.text

    @staticmethod
    @pytest.mark.positive
    def test003(start_browser):
        """
        Test type - positive
        Edit product
        :param start_browser: browser run
        """
        driver = start_browser
        authorize_as_admin(driver, login="admin", password="admin")
        add_new_product(driver,
                        product_name="Test product",
                        meta_tag="Test meta tag",
                        model="Test model")
        filter_products_by_name(driver, product_name="Test product")
        ProductPage.find_and_click_edit_button(driver)
        ProductPage.clear_product_name_field(driver)
        ProductPage.input_product_name(driver, product_name="Edited test product")
        ProductPage.save_new_product_button_click(driver)
        ProductPage.clear_filter_name_filed(driver)
        filter_products_by_name(driver, product_name="Edited test product")
        products = ProductPage.find_product_name(driver)
        for product in products:
            assert "Edited test product" in product.text
        filter_products_by_name(driver, product_name="Edited test product")
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)

    @staticmethod
    @pytest.mark.positive
    def test004(start_browser):
        """
        Test type - positive
        Create new product with 3 img
        :param start_browser: browser run
        """
        driver = start_browser
        images_names = ("1", "2", "3")
        jpg_names = list()
        for name in images_names:
            jpg_names.append(str(name)+".jpg")
        authorize_as_admin(driver, login="admin", password="admin")
        add_new_product_with_images(driver,
                                    product_name="Test product",
                                    meta_tag="Test meta tag",
                                    model="Test model",
                                    images_path="/home/vasiliev_va/Downloads/special/",
                                    file_names=jpg_names)
        ProductPage.check_images_names(driver, images_names)
        delete_images_from_opencart(driver, file_names=jpg_names)
        MainPage.open_product_catalog(driver)
        MainPage.click_product_button(driver)
        filter_products_by_name(driver, product_name="Test product")
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)

    @staticmethod
    @pytest.mark.positive
    def test005(start_browser):
        """
        Test type - positive
        add new menu field and drug and drop it
        :param start_browser: browser run
        """
        driver = start_browser
        demo_authorize(driver, login="demo", password="demo")
        add_new_menu_field(driver)
        ConstructorMenu.check_computer_element(driver)
