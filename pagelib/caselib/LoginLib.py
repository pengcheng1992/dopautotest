# -*- coding:utf8 -*-
# Author:Pengcheng
from pagelib.baselib.Element import  pucom
from pageobj.LoginObj import loginobj
from testdata.BaseData import ld
from nose.tools import *



class LoginLib(object):
    def logindop(self,msg=None):
        pucom.info(msg)
        pucom.click_if_exist(loginobj.login_chose_up)
        pucom.set_value(loginobj.username_input,ld.userinfo()["username"])
        pucom.set_value(loginobj.password_input,ld.userinfo()["password"])
        pucom.click_if_exist(loginobj.login_button,1)
        pucom.info("判断是否登录成功")

    def verify_UserName(self,msg=None):
        pucom.info(msg)
        assert_equal(pucom.get_text(loginobj.real_name), ld.userinfo()["realname"], "登录失败")
        pucom.info("登录成功")


login = LoginLib()