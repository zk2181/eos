#!/usr/bin/env Python
# coding=utf-8

from db import *

def creat_table(tablename):
    sql = "RENAME TABLE new TO last" + tablename + ";"
    cur.execute(sql)
    lines = cur.fetchall()
    #sql = "create table " + tablename + "(id int(2) not null primary key auto_increment,sysid text not null,sysname text,schdtime int(2),priolevel int(1),difflevel int(1))default charset=utf8;"
    sql = "create table new(id int(2) not null primary key auto_increment,sysid text not null,sysname text,schdtime int(2),priolevel int(1),difflevel int(1))default charset=utf8;"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def creat_colums(syscode, sysname ):
    sql = "insert into news(sysid, sysname) values ("+sysid+","+sysname+");"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines;
