#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import methods.writedb as mwd

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
    #    print "type(one_user)"
        self.render("admin.html")
    def post(self):
        tabledate = self.get_argument("htmldate")
        #table_infos = mwd.creat_table(tablename="new")
        table_infos = mwd.creat_table(tablename=tabledate)
        #self.write(table_infos)
        self.redirect('/admin')
