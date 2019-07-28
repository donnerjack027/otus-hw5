#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging as log
import pytest
import allure
from library.subproc import SPUser


class TestSuiteHw26:
    """homework 26"""
    @staticmethod
    @allure.title("Critical: Cpu workload")
    @allure.severity("critical")
    @pytest.mark.critical
    def test001():
        """
        Cpu workload
        """
        with allure.step("Input command"):
            process = SPUser()
            command = "sensors | grep Core | awk '{print $3}'"
            output = process.check_output(command)
        with allure.step("Parse cpu temperature"):
            process.byte_parser(output)
        with allure.step("Checking temperature"):
            process.temperature_checker()

    # @staticmethod
    # @allure.title("Critical: Cpu info")
    # @allure.severity("critical")
    # @pytest.mark.critical
    # def test002():
    #     """
    #     Cpu info
    #     """
    #     with allure.step("Input command"):
    #         process = SPUser()
    #         command = "cat /proc/cpuinfo"
    #         output = process.check_output(command)
    #     with allure.step("Parse cpu information"):
    #         process.byte_parser(output)
    #         process.cpu_info_model_parser()
    #     with allure.step("Checking cpu information"):
    #         cpu_parameters = ['Intel(R)', 'Core(TM)', 'i3-6100']
    #         process.cpu_info_checker(*cpu_parameters)
    #
    # @staticmethod
    # @allure.title("Critical: enp1s0 status")
    # @allure.severity("critical")
    # @pytest.mark.critical
    # def test003():
    #     """
    #     enp1s0 status
    #     """
    #     with allure.step("Input command"):
    #         process = SPUser()
    #         command = "ip a | grep enp1s0"
    #         output = process.check_output(command)
    #     with allure.step("Parse main interface state"):
    #         process.byte_parser(output)
    #         process.interface_state_parser()
    #     with allure.step("Checking that main interface is UP"):
    #         process.interface_status_checker()
    #
    # @staticmethod
    # @allure.title("Critical: Default route")
    # @allure.severity("critical")
    # @pytest.mark.critical
    # def test004():
    #     """
    #     Default route
    #     """
    #     with allure.step("Input command"):
    #         process = SPUser()
    #         command = "ip r | grep default"
    #         output = process.check_output(command)
    #     with allure.step("Parse default route data"):
    #         process.byte_parser(output)
    #     with allure.step("Checking default route state"):
    #         process.default_route_checker(default_ip='192.168.0.254', default_method='dev')

    @staticmethod
    @allure.title("Critical: Process resource costs")
    @allure.severity("critical")
    @pytest.mark.critical
    def test005():
        """
        Process resource costs
        """
        with allure.step("Input command"):
            process = SPUser()
            command = "ps aux | awk '{print $3}'"
            output = process.check_output(command)
        with allure.step("Parse process information"):
            coast = process.byte_parser(output)
            parsed_coast = coast[1:]
        with allure.step("Checking resource costs"):
            process.process_coast_checker(parsed_coast)

    # @staticmethod
    # @allure.title("Critical: Web interfaces statistic")
    # @allure.severity("critical")
    # @pytest.mark.critical
    # def test006():
    #     """
    #     Web interfaces statistic
    #     """
    #     with allure.step("Input command"):
    #         process = SPUser()
    #         command = "ifconfig"
    #         output = process.check_output(command)
    #     with allure.step("Parse ifconfig statistic"):
    #         ifconfig = process.byte_parser(output)
    #     with allure.step("Print and logging statistic"):
    #         print(ifconfig)
    #         log.info("Interface statistic: %s", ifconfig)
    #
    # @staticmethod
    # @allure.title("Critical: Service status")
    # @allure.severity("critical")
    # @pytest.mark.critical
    # def test007():
    #     """
    #     Service status
    #     """
    #     with allure.step("Input command"):
    #         service_name = "ssh"
    #         process = SPUser()
    #         command = "service %s status | grep Active", service_name
    #         output = process.check_output(command)
    #     with allure.step("Parse ifconfig statistic"):
    #         process.byte_parser(output)
    #     with allure.step("Checking service status"):
    #         process.service_status_checker()

    @staticmethod
    @allure.title("Critical: Tcp/udp port status")
    @allure.severity("critical")
    @pytest.mark.critical
    def test008():
        """
        Tcp/udp port status
        """
        with allure.step("Input command"):
            process = SPUser()
            command = "netstat -ntlp | grep LISTEN | awk '{print $4}'"
            output = process.check_output(command)
        with allure.step("Parse port statistic"):
            port_statistic = process.byte_parser(output)
        with allure.step("Printing and logging udp/tcp ports with LISTEN status"):
            print(port_statistic)
            log.info("UDP/TCP ports with LISTEN status: %s", port_statistic)

    @staticmethod
    @allure.title("Critical: Package version")
    @allure.severity("critical")
    @pytest.mark.critical
    def test009():
        """
        Package version
        """
        with allure.step("Input command"):
            package_name = "php-curl"
            process = SPUser()
            command = "dpkg --list | grep %s | awk '{{print $3}}'", package_name
            output = process.check_output(command)
        with allure.step("Parse package version"):
            package_version = process.byte_parser(output)
        with allure.step("Printing and logging package version"):
            print(package_version)
            log.info("Package %s has version %s", (package_name, package_version))

    @staticmethod
    @allure.title("Critical: Files in directory")
    @allure.severity("critical")
    @pytest.mark.critical
    def test010():
        """
        Files in directory
        """
        with allure.step("Input command"):
            directory = "/home/vasiliev_va/Documents"
            command = "cd %s; ls -l", directory
            process = SPUser()
            output = process.check_output(command)
        with allure.step("Parse directory content"):
            content = process.byte_parser(output)
        with allure.step("Printing and logging directory content"):
            print(content)
            log.info("Directory with path '%s' has content '%s'",(directory, content))

    @staticmethod
    @allure.title("Critical: Current directory")
    @allure.severity("critical")
    @pytest.mark.critical
    def test011():
        """
        Current directory
        """
        with allure.step("Input command"):
            command = "echo $PWD"
            process = SPUser()
            output = process.check_output(command)
        with allure.step("Parse current directory information"):
            dir_info = process.byte_parser(output)
        with allure.step("Printing and logging current directory path"):
            print(dir_info)
            log.info("Current directory path: %s", dir_info)

    @staticmethod
    @allure.title("Critical: Core version")
    @allure.severity("critical")
    @pytest.mark.critical
    def test012():
        """
        Core version
        """
        with allure.step("Input command"):
            command = "uname -a"
            process = SPUser()
            output = process.check_output(command)
        with allure.step("Parse core information"):
            core_info = process.byte_parser(output)[2]
        with allure.step("Printing and logging core info"):
            print(core_info)
            log.info("Core version is: %s", core_info)

    @staticmethod
    @allure.title("Critical: Operation system version")
    @allure.severity("critical")
    @pytest.mark.critical
    def test013():
        """
        Operation system version
        """
        with allure.step("Input command"):
            command = " lsb_release -a | grep Description | awk '{print $2 $3 $4}'"
            process = SPUser()
            output = process.check_output(command)
        with allure.step("Parse operation system information"):
            os_info = process.byte_parser(output)
        with allure.step("Printing and logging operation system info"):
            print(os_info)
            log.info("Core version is: %s", os_info)
