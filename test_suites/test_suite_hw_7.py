#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Test Suite - homework 7
"""

import pytest
from library.keywords import authorize_as_admin, add_new_product, \
    filter_products_by_name, delete_all_products
from library.pages.product_page import ProductPage


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
