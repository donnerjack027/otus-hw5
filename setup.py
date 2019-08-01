#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from setuptools import setup, find_packages


setup(name='otus-project',
      version='1.0',
      url='https://github.com/Donnerjack027/otus-hw5',
      license='MIT',
      author='Vasiliev Victor',
      author_email='vasiliev_va@protei.ru',
      description='Otus tests',
      long_description=open('README.md').read(),
      setup_requires=['pytest>=4.4.0'],
      zip_safe=False)
