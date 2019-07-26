#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
Parametrization class
"""


class Parametrization:
    """
    Parametrization methods
    """
    def __init__(self):
        self.method = None
        self.headline = None
        self.host = None
        self.port = None
        self.headline_data = None

    def get_method(self):
        """
        Input method or press Enter to default
        """
        self.method = input("Please enter method or press Enter to default...")
        if self.method == '':
            self.method = "GET"
        return self.method

    def get_headline(self):
        """
        Input headline or press Enter to default
        """
        self.headline = input("Please enter headline or press Enter to default...")
        if self.headline != '':
            self.headline_data = input("Please enter headline data...")
        if self.headline == '':
            self.headline = "Host"
            self.headline_data = "localhost"
        return self.headline, self.headline_data

    def get_host(self):
        """
        Input host or press Enter to default
        """
        self.host = input("Please enter host or press Enter to default...")
        if self.host == '':
            self.host = "youtube.com"
        return self.host

    def get_port(self):
        """
        Input port or press Enter to default
        """
        self.port = input("Please enter port or press Enter to default...")
        if self.port == '':
            self.port = 80
        return self.port
