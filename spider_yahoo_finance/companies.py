# -*- coding: utf-8 -*-
__author__ = 'seany'


class Companies():
    def __init__(self):
        self.dict = {}


class Company():
    def __init__(self, stock_name, stock_price, pe):
        self.stock_name = stock_name
        self.stock_price = stock_price
        self.pe = pe

    def __str__(self):
        return self.stock_name + "   " + \
               self.stock_price + "   " + \
               self.pe

if __name__ == "__main__":
    print "This is main"