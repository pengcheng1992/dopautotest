# -*- coding:utf8 -*-
#  Author:pengcheng


from pagelib.baselib.Element import pucom
from pagelib.caselib.LoginLib import login
from pagelib.caselib.NewStrategyLib import nsl
# 登录dop首页
class TestDopNewStrategy(object):

    def setUp(self):
        pucom.info("============test class setup==============")
        pucom.open_browser("http://qadop.hujiang.com/marketing/","打开浏览器并跳转到dop首页")
        login.logindop("step1:以用户名密码登录dop")
        login.verify_UserName("step2:检查是否登录成功")


    def teardown(self):
        pucom.close_browser()
        pucom.info("============test class teardown==============\n\n")

        # 添加每天策略
    def test001_new_everyday_strategy(self):
        pucom

        # 添加每周策略
    def test002_new_weekday_strategy(self):
        pucom

        # 添加每月策略
    def test003_new_monthly_strategy(self):
        pucom

        #添加一次性策略
    def test004_new_disposable_strategy(self):
        pucom

