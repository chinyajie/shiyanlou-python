# /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime
from collections import Counter


def open_parser(filename):
    with open(filename) as logfile:
        pattern = (
            '(\d+.\d+.\d+.\d+)\s-\s-\s'
            '\[(.+)\]\s'
            '"GET\s(.+)\s\w+/.+"\s'
            '(\d+)\s'
            '(\d+)\s'
            '"(.+)"\s'
            '"(.+)"'
        )
        parsers = re.findall(pattern, logfile.read())

    ip_list = []
    request404_list = []

    for item in parsers:
        dt = datetime.strptime(item[1][:-6], "%d/%b/%Y:%H:%M:%S")
        if dt.strftime("%d%b%Y") == '11Jan2017':
            ip_list.append(item[0])
        if int(item[3]) == 404:
            request404_list.append(item[2])
    return ip_list, request404_list


def main():
    ip_list, url_list = open_parser('/home/shiyanlou/Code/nginx.log')
    ip_counts = Counter(ip_list)
    url_counts = Counter(url_list)

    ip_sorted = sorted(ip_counts.items(), key=lambda x: x[1])
    url_sorted = sorted(url_counts.items(), key=lambda x: x[1])
    print((dict([ip_sorted[-1]]), dict([url_sorted[-1]])))  # []


if __name__ == '__main__':
    main()
