# coding: utf-8 ##

# __author__ = 'seany'


# 获取公司的信息#
# http://finance.yahoo.com/q?s=NVDA
import urllib2
import re
import sys
import os
import companies
import store_in_database


def get_company_info(stock_name):
    # 获取当前系统编码格式
    code_type = sys.getfilesystemencoding()
    url = 'http://finance.yahoo.com/q?s='
    url = url + stock_name
    # 读取url内容
    content = urllib2.urlopen(url).read()
    # 转换编码
    content = content.decode("UTF-8").encode(code_type)
    # read stock price
    reg = r'<span id="yfs_l84_' + stock_name.lower() + r'">(\d*\.\d*)</span>'
    m = re.search(reg, content)
    stock_price = m.group(1)
    # read pe
    # <td class="yfnc_tabledata1">18.72</td>
    reg = r'<td class="yfnc_tabledata1">([\d\.]*)</td>'
    m = re.search(reg, content)
    pe = m.group(1)
    # read eps
    # <td class="yfnc_tabledata1">1.12</td>
    # reg = r'<span id="yfs_l84_' + stock_name.lower() + r'>([\d\.]*)</span>'
    # eps = re.compile(reg, re.I).search(content).group(1)
    # # read days_range
    # reg = r'<span id="yfs_l84_' + stock_name.lower() + r'>([\d\.]*)</span>'
    # days_range = re.compile(reg, re.I).search(content).group(1)
    # # read volume
    # reg = r'<span id="yfs_l84_' + stock_name.lower() + r'>([\d\.]*)</span>'
    # volume = re.compile(reg, re.I).search(content).group(1)
    #return companies.Company(stock_name, stock_price, pe, eps, days_range, volume)
    return companies.Company(stock_name, stock_price, pe)


def read_company_stock():
    current_path = os.getcwd()
    company_stock_file = current_path + "/" + "company_stock"
    company_stock_dict = {}
    if os.path.exists(company_stock_file):
        with open(company_stock_file, "r") as FILE:
            for line in FILE.readlines():
                if re.match(r'^\s*$', line):
                    pass
                elif re.match(r"#", line):
                    pass
                else:
                    m = re.match(r"\s*(\w[\w\s]*)\s+(\w+)$", line)
                    company_name = m.group(1)
                    stock_name = m.group(2)
                    company_stock_dict[company_name] = stock_name
    return company_stock_dict


def get_info():
    company_stock_dict = read_company_stock()
    company_list = companies.Companies()
    for key in company_stock_dict.keys():
        company_list.dict[key] = get_company_info(company_stock_dict[key])
    return company_list


if __name__ == "__main__":
    my_list = get_info()
    print "Company_name   " + "Stock_name   " + "Stock_price   " + "P/E"
    for key in my_list.dict.keys():
        print key + "   ",
        print my_list.dict[key]