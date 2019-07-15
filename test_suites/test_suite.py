#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging


def test_run(start_browser, open_login_page):
    start_browser.get(open_login_page)
    current_url = start_browser.current_url
    parametrized_url = open_login_page
    logging.debug("Parametrized url is {}".format(parametrized_url))
    logging.debug("Current url is {}".format(current_url))
    assert parametrized_url == current_url
