#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
Simple test check
"""
import requests


def test_check():
    response = requests.get("http://192.168.110.60/opencart/")
    if response.ok:
        return response
    else:
        return None
