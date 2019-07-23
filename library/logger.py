#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
selenium logger
"""
import logging as log
from selenium.webdriver.support.events import AbstractEventListener


class OpencartListener(AbstractEventListener):
    """
    selenium logger
    """
    log.basicConfig(filename='test_run_log.log', level=log.disable(10))

    def before_find(self, by, value, driver):
        """
        logging before find
        """
        log.info("trying to find by%s:%s", (by, value))

    def after_find(self, by, value, driver):
        """
        logging after find
        """
        log.info(by, value, "element found!")

    def before_click(self, element, driver):
        """
        logging before click
        """
        log.info("trying to click on %s", element)

    def after_click(self, element, driver):
        """
        logging after click
        """
        log.info("click on %s has been success!", element)

    def on_exception(self, exception, driver):
        """
        logging on exception
        """
        driver.save_screenshot("./exception_screenshot.png")
        log.error(exception)

    def before_quit(self, driver):
        """
        logging before quit
        """
        log.info("Starting browser")

    def after_quit(self, driver):
        """
        logging after quit
        """
        log.info("Quiting browser")


def web_logging(driver, log_file="web_log.log"):
    """
    Browser logging function
    :param driver: browser web driver
    :param log_file: path to the log file
    """
    web_logs = open(log_file, 'w')
    for string in driver.get_log("performance"):
        web_logs.write(string + '\n')
    web_logs.close()


def proxy_logging(proxy, log_file="proxy_log.log"):
    """
    Proxy logging function
    :param proxy: browsermob proxy
    :param log_file: path to the log file
    """
    proxy_logs = open(log_file, 'w')
    proxy_logs.write(str(proxy.har))
    proxy_logs.close()
