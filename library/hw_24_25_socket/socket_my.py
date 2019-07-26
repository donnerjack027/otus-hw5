#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
Socket class
"""

import socket
from parser_html import MyHTMLParser
from parametrization import Parametrization


class Socket:
    """
    Socket methods
    """
    def __init__(self):
        self.parametrization = Parametrization()
        self.host = self.parametrization.get_host()
        self.port = self.parametrization.get_port()
        self.method = self.parametrization.get_method()
        self.headline, self.headline_data = self.parametrization.get_headline()

    def socket_connect(self):
        """
        Connect
        """
        request = "{} / HTTP/1.1\n{}: {}\n\n".format(self.method,
                                                     self.headline,
                                                     self.headline_data)
        address = (self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        sock.send(request.encode())
        result = sock.recv(4096)
        data = (result.decode(encoding="ISO-8859-1"))
        sock.close()
        return data

    def dict_data_parser(self):
        """
        dict parser
        """
        some_data = (self.socket_connect().split('\n'))
        final_dict = dict()
        for i in some_data:
            new_str = i.split()
            if len(new_str) > 1:
                final_dict[new_str[0]] = new_str[1:]
            else:
                continue
        for keys, values in final_dict.items():
            print(keys, values)

    def html_data_parser(self):
        """
        html parser
        """
        parser = MyHTMLParser()
        parser.feed(self.socket_connect())
        parser.print_all()
