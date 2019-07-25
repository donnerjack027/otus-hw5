#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pytest
import allure
from library.ftp import RunCommandFtp
from library.ssh import RunCommandSSH


class TestSuiteHw22:
    """homework 22-23"""
    @staticmethod
    @allure.title("Critical: Restart apache service")
    @allure.severity("critical")
    @pytest.mark.critical
    @pytest.mark.positive
    def test001():
        """
        Restart apache2 service
        """
        with allure.step("Connecting to remote zone"):
            ssh = RunCommandSSH(host='192.168.110.60',
                                username='support',
                                password='elephant',
                                port='22')
        with allure.step("Restarting apache2 service"):
            ssh.service_restart(service='apache2')
        with allure.step("Checking apache2 service status"):
            ssh.service_status_check(service='apache2')

    @staticmethod
    @allure.title("Critical: Restart mysql service")
    @allure.severity("critical")
    @pytest.mark.critical
    @pytest.mark.positive
    def test002():
        """
        Restart mysql service
        """
        with allure.step("Connecting to remote zone"):
            ssh = RunCommandSSH(host='192.168.110.60',
                                username='support',
                                password='elephant',
                                port='22')
        with allure.step("Restarting mysql service"):
            ssh.service_restart(service='mysql')
        with allure.step("Checking mysql service status"):
            ssh.service_status_check(service='mysql')

    @staticmethod
    @allure.title("Critical: Creating new directory on ftp server, then - remove")
    @allure.severity("critical")
    @pytest.mark.critical
    @pytest.mark.positive
    def test003():
        """
        Add new directory, then - remove
        """
        with allure.step("Connecting to ftp server"):
            ftp = RunCommandFtp(address='192.168.110.60',
                                login='support',
                                password='elephant')
            ftp.connect()
        try:
            with allure.step("Authorizing"):
                ftp.authorize()
            with allure.step("Changing directory"):
                ftp.change_directory(path='support')
            with allure.step("Creating directory"):
                ftp.create_directory(dir_name='Test_dir')
            with allure.step("Checking directory"):
                ftp.check_directory(dir_name='Test_dir')
        finally:
            with allure.step("Removing directory and disconnect from ftp server"):
                ftp.remove_directory(dir_name='Test_dir')
                ftp.close_connection()
