# -*- coding:utf8 -*-
# create by pengcheng
class HomeObj(object):
    strategy_manage = "//div/i[contains(@class,'fa fa-book')]/.."        #策略管理按钮
    push_strategy = "//phx-sidenav-item[@ng-reflect-link='/strategy/push']"     #推送策略按钮
    customer = "//label[text()='客户']/following-sibling::*//div"     #客户下拉框
    basic_customer = "//phx-select-option[text()='基础-测试客户']"        #基础客户选项
    user_crowd = "//label[text()='用户群']/following-sibling::*//div"      #用户群下拉框
    basic_user_crowd = "//phx-select-option[text()='自动化导入人群——基础(10339)']"       #用户群的自动化导入人群
    crowd = "//label[text()='人群']/following-sibling::*//div"        #人群下拉框
    import_crowd = "//phx-select-option[text()='导入人群']"     #导入人群

homeobj =  HomeObj()