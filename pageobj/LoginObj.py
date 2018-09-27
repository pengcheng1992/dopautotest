# -*- coding:utf8 -*-
# Author:Pengcheng

class LoginObj(object):
    login_chose_up = "//*[@id='hp-pass-box']//button[contains(text(),'帐号密码登录')]"        #账号密码登录按钮
    username_input = "//*[@id='nameInput']"     #用户名输入框
    password_input = "//*[@id='passInput']"     #密码输入框
    login_button = "//button[contains(text(),'登录')]"      #登录按钮
    real_name = "//phx-header-item[@class='phx-header-item-auto phx-header-item phx-header-item-right']/span"       #真实名字

loginobj = LoginObj()