# -*- coding:utf8 -*-
# Author:Pengcheng
from pagelib.baselib.Element import  pucom
from pageobj.LoginObj import loginobj


class LoginLib(object):
    def logindop(self,msg=None):
        pucom.click_if_exist(loginobj.login_chose_up)
        pucom.set_value(loginobj.username_input,"pengcheng2819")
        pucom.set_value(loginobj.password_input,"pengcheng2819")
        pucom.click_if_exist(loginobj.login_button)

    def verify_UserName(self,msg=None):
        # puCom.infoBold(msg)
        # actual = puCom.element._get_value(Login.real_name)
        # if actual == self.user['realname'] :
        #     puCom.infoBold("登录成功！")
        # else:
        #     puCom.infoBold("登录失败！")
        #     raise RuntimeError("登录失败")
        return


login = LoginLib()