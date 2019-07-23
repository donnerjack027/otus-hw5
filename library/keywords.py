#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
keywords page
"""

from library.pages.product_page import ProductPage
from library.pages.main_page import MainPage
from library.pages.admin_page import AdminPage


def authorize_as_admin(driver, login, password):
    """
    Keyword - auth as admin
    """
    AdminPage.login_input(driver, login)
    AdminPage.password_input(driver, password)
    AdminPage.accept_button_click(driver)
    MainPage.message_close_button_click(driver)


def add_new_product(driver, product_name, meta_tag, model):
    """
    Keyword - add product
    """
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.input_product_name(driver, product_name)
    ProductPage.input_meta_tag(driver, meta_tag)
    ProductPage.data_tab_click(driver)
    ProductPage.input_model(driver, model)
    ProductPage.save_new_product_button_click(driver)


def filter_products_by_name(driver, product_name):
    """
    Keyword - filter product by name
    """
    ProductPage.input_product_name_to_filter(driver, product_name)
    ProductPage.click_filter_button(driver)


def delete_all_products(driver):
    """
    Keyword - del all products
    """
    ProductPage.click_choose_all_products_checkbox(driver)
    ProductPage.click_delete_all_products_button(driver)


def add_new_product_with_images(driver, product_name, meta_tag, model, images_path, file_names):
    """
    Keyword - add product with img
    """
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.input_product_name(driver, product_name)
    ProductPage.input_meta_tag(driver, meta_tag)
    ProductPage.data_tab_click(driver)
    ProductPage.input_model(driver, model)
    ProductPage.click_on_image_tab(driver)
    ProductPage.click_on_image(driver)
    ProductPage.click_on_edit_image_button(driver)
    ProductPage.add_new_images_to_store(driver, images_path, *file_names)
    ProductPage.close_add_image_menu()
    ProductPage.add_images_to_product(driver, *file_names)


def delete_images_from_opencart(driver, file_names):
    """
    Keyword - delete all images from opencart
    """
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.click_on_image_tab(driver)
    ProductPage.click_on_image(driver)
    ProductPage.click_on_edit_image_button(driver)
    ProductPage.choose_remove_images_by_names(driver, file_names)
    ProductPage.delete_selected_images(driver)
    ProductPage.close_add_image_menu()
