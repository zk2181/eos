#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user='root', passwd='123', db='zktest', port=3306, charset="utf8")

cur = conn.cursor()
