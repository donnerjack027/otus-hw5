#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from collections import Counter
import itertools
import json
import re
import logging
import os


def request_collector(filename):
    with open(filename) as log_file:
        request_list = ("GET", "POST", "OPTIONS", "HEAD", "PUT", "PATCH", "DELETE", "TRACE", "CONNECT")
        log = log_file.read()
        ips_list = list()
        for resp in request_list:
            for i in re.findall(resp, log):
                ips_list.append(i)
        return ips_list


def top_ten_ip_collector(filename):
    with open(filename) as log_file:
        log = log_file.read()
        ip_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
    return Counter(ip_list).most_common(10)


def top_ten_duration_request(filename):
    with open(filename) as log_file:
        my_list = list()
        duration_error_dict = dict()
        return_dict = dict()
        for line in log_file:
            my_list.append(line.split(' '))
        for i in my_list:
            duration_error_dict[i[9]] = i[0:8]
        for j in itertools.islice(sorted(duration_error_dict, reverse=True), 10):
            return_dict[j] = duration_error_dict[j]
        return return_dict


def top_ten_client_errors(filename):
    with open(filename) as log_file:
        my_list = list()
        client_error_list = list()
        for line in log_file:
            my_list.append(line.split(' '))
        for i in my_list:
            if int(i[8][0]) == 4:
                client_error_list.append(i)
    return client_error_list


def top_ten_server_errors(filename):
    with open(filename) as log_file:
        my_list = list()
        server_error_list = list()
        for line in log_file:
            my_list.append(line.split(' '))
        for i in my_list:
            if int(i[8][0]) == 5:
                server_error_list.append(i)
    return server_error_list


def count(ips_list):
    count_list = Counter(ips_list)
    return count_list


def use_parser(log_file):
    try:
        req = "{}:{}".format("Requests list", count(request_collector(log_file)))
        ip = "{}:{}".format("Top ten ip", top_ten_ip_collector(log_file))
        dur_req = "{}:{}".format("Top ten requests by duration", top_ten_duration_request(log_file))
        client_err = "{}:{}".format("Top client errors", top_ten_client_errors(log_file))
        server_err = "{}:{}".format("Top server errors", top_ten_server_errors(log_file))
        with open(str(log_file) + '.json', 'w') as output:
            json.dump((ip, req, dur_req, client_err, server_err), output)
    except(FileNotFoundError, FileExistsError):
        logging.error("Can't read file : {}!".format(log_file))


if __name__ == '__main__':
    content_type = input("Input file or file_path (or press Enter for default path): ")
    if content_type == '':
        content_type = 'access.log'
    if content_type.endswith('.log'):
        use_parser(log_file=content_type)
    else:
        file_list = os.listdir(content_type)
        for file in file_list:
            if file.startswith('access') and '.log' in file:
                if not file.endswith('.gz'):
                    use_parser(file)
