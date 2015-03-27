# coding=utf-8 ##
__author__ = 'seany'

import re


s = '<span class="pl">(164人评价)</span>'
print s
a = re.findall(r'<span class="pl">\((\d+)'.encode("gbk"), s)
print a

