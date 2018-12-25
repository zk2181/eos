#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        user_infos = mrd.select_columns(table="news",column="*")
        self.render("list.html", new = user_infos)
