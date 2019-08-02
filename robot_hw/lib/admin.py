#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from robot.api.deco import keyword
from selenium import webdriver


class Admin:
    @keyword(name="Admin opencart test")
    def admin_opencart_login(self):
        driver = webdriver.Firefox()
        driver.get('http://192.168.110.60/opencart/admin/')
        driver.find_element_by_id("input-username").send_keys("admin")
        driver.find_element_by_id("input-password").send_keys("admin")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            driver.find_element_by_xpath("//button[@class='close']").click()
        except Exception:
            print("There are no alert! May be u didn't login?")
        finally:
            driver.close()
