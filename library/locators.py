#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
locators
"""

from selenium.webdriver.common.by import By


class Locators:
    """
    locators
    """
    login_input_locator = (By.ID, "input-username")
    password_input_locator = (By.ID, "input-password")
    login_button_locator = (By.CLASS_NAME, "btn.btn-primary")
    message_close_button_locator = (By.CLASS_NAME, "close")
    product_catalog_locator = (By.ID, "menu-catalog")
    product_button_locator = (By.LINK_TEXT, "Products")
    add_new_product_locator = (By.CLASS_NAME, "btn.btn-primary")
    name_input_field_locator = (By.ID, "input-name1")
    meta_title_locator = (By.ID, "input-meta-title1")
    data_tab_locator = (By.XPATH, "//a[@href='#tab-data']")
    model_input_field_locator = (By.ID, "input-model")
    save_new_product_button_locator = (By.CLASS_NAME, "btn.btn-primary")
    product_form_locator = (By.CLASS_NAME, "table.table-bordered.table-hover")
    product_name_filter_locator = (By.ID, "input-name")
    filter_button_locator = (By.ID, "button-filter")
    checkboxes_locator = (By.CSS_SELECTOR, "input")
    delete_products_locator = (By.CLASS_NAME, "btn.btn-danger")
    edit_product_button_locator = (By.CLASS_NAME, "btn.btn-primary")
