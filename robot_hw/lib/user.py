#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from robot.api.deco import keyword
from selenium import webdriver


class User:
    @keyword(name="User opencart test")
    def user_opencart_login(self):
        driver = webdriver.Firefox()
        driver.get('http://192.168.110.60/opencart/')
        driver.find_element_by_xpath("//a[@title='My Account']").click()
        driver.find_element_by_xpath("//a[@href='http://192.168.110.60/"
                                     "opencart/index.php?route=account/login']").click()
        driver.find_element_by_xpath(".//*[@id='input-email']").send_keys("support@localhost.ru")
        driver.find_element_by_xpath(".//*[@id='input-password']").send_keys("support")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.find_element_by_xpath("//a[@title='My Account']").click()
        try:
            driver.find_element_by_xpath("//a[@href='http://192.168.110.60/"
                                         "opencart/index.php?route=account/logout']").click()
        except Exception:
            print("There are no logout button! May be u didn't login?")
        finally:
            driver.close()
