#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        usernames = mrd.select_columns(table="users",column="username,email")
        #one_user = usernames[0][0]
        one_user = usernames
	print "type(one_user)"
        self.render("admin.html", user=one_user)
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
	if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write(username)
