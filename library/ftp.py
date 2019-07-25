#!/usr/bin/python
# -*- coding: UTF-8 -*-


import ftplib
import logging as log


class RunCommandFtp:
    def __init__(self, address, login, password):
        self.address = address
        self.auth = {"user": login,
                     "passwd": password}
        self.connection = None

    def connect(self):
        self.connection = ftplib.FTP(self.address)

    def authorize(self):
        self.connection.login(**self.auth)

    def change_directory(self, path):
        self.connection.cwd(path)

    def create_directory(self, dir_name):
        self.connection.mkd(dir_name)

    def check_directory(self, dir_name):
        directory_list = list()
        self.connection.retrlines("LIST", directory_list.append)
        string = directory_list[0].split()
        if dir_name not in string:
            log.error("There are no directory with name {}".format(dir_name))
            raise Warning("There are no directory with name {}".format(dir_name))
        else:
            log.info("Directory with name {} find!".format(dir_name))

    def remove_directory(self, dir_name):
        self.connection.rmd(dir_name)

    def close_connection(self):
        self.connection.close()
