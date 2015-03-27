# -*- coding: utf-8 -*-

__author__ = 'seany'


import sqlite3

conn = sqlite3.connect("database_name")

cur = conn.cursor()

cmd = ".TABLES"
result = cur.execute(cmd)
print result