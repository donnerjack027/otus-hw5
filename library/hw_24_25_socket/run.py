#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
Socket runner
"""
from socket_my import Socket


socket = Socket()


temp = input('Press "1" for html_parser, Press "2" for dict_parser: \n')
if temp == "1":
    socket.html_data_parser()
elif temp == "2":
    socket.dict_data_parser()
else:
    raise Exception('Input error!')
