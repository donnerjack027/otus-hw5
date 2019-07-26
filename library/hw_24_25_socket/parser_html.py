#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
HTMLParser class
"""

from abc import ABCMeta
from html.parser import HTMLParser
from collections import Counter


class MyHTMLParser(HTMLParser, metaclass=ABCMeta):
    """
    HTMLParser methods
    """
    def __init__(self):
        super().__init__()
        self.tag_dict = dict()
        self.tag_list = list()
        self.final_dict = dict()
        self.most_frequent_tag = str()
        self.text_list = list()
        self.href_list = list()

    def handle_starttag(self, tag, attrs):
        """
        Handle starttag
        """
        self.tag_dict[tag] = attrs
        if len(attrs) > 0:
            self.tag_list.append(tag)

    def tag_parser(self):
        """
        Tag parser
        """
        count_dict = Counter(self.tag_list)
        counter = 0
        for key, value in count_dict.items():
            if counter < value:
                counter = value
                self.most_frequent_tag = key
            else:
                continue

    def text_parser(self):
        """
        Text parser
        """
        for i in range(1, 6):
            if 'h{}'.format(i) in self.tag_dict.keys():
                self.text_list.append(self.tag_dict['h{}'.format(i)])

    def href_parser(self):
        """
        Href parser
        """
        if 'a' in self.tag_dict.keys():
            if self.tag_dict['a'][0][0].strip() == "href":
                self.href_list.append(self.tag_dict['a'][0][1].strip())

    def final_dict_creator(self):
        """
        Final creator
        """
        self.final_dict['tags'] = self.tag_list
        self.final_dict['text'] = self.text_list
        self.final_dict['most_frequent_tag'] = self.most_frequent_tag
        self.final_dict['images and urls'] = self.href_list

    def print_all(self):
        """
        Print
        """
        self.href_parser()
        self.tag_parser()
        self.text_parser()
        self.final_dict_creator()
        print(self.final_dict)
