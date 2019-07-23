#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
keywords page
"""

from library.pages.product_page import ProductPage
from library.pages.main_page import MainPage
from library.pages.admin_page import AdminPage
from library.constructor_menu import ConstructorMenu
from library.pages.downloads_page import DownloadsPage


def authorize_as_admin(driver, login, password):
    """
    Keyword - auth as admin
    """
    AdminPage.login_input(driver, login)
    AdminPage.password_input(driver, password)
    AdminPage.accept_button_click(driver)
    MainPage.message_close_button_click(driver)


def demo_authorize(driver, login, password):
    """
    Keyword - auth as admin on demo23.opencart.pro
    """
    AdminPage.login_input(driver, login)
    AdminPage.password_input(driver, password)
    AdminPage.accept_button_click(driver)


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


def add_new_menu_field(driver):
    """
    Keyword - add new menu
    """
    MainPage.click_design_menu(driver)
    MainPage.click_menu_constructor(driver)
    ConstructorMenu.drug_computer_drop_components(driver)


def add_file_to_opencart(driver, file_url, file_name):
    """
    Keyword - add file to opencart
    """
    MainPage.open_product_catalog(driver)
    MainPage.click_downloads_button(driver)
    DownloadsPage.click_add_new_file(driver)
    DownloadsPage.input_download_file_name(driver, file_name)
    DownloadsPage.download_file(driver, file_url)
    DownloadsPage.check_downloaded_file(driver, file_name)
