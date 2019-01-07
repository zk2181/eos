#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import methods.writedb as mwd

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        user_infos = mrd.select_columns(table="news",column="*")
        self.render("list.html", new = user_infos)
    def post(self):
        syscode = self.get_argument("syscode")
        sysname = self.get_argument("sysname")
        user_infos = mwd.creat_colums(syscode=syscode,sysname=sysname)
        #if user_infos:
        #    db_pwd = user_infos[0][2]
        #    if db_pwd == password:
        #        self.write(username)
