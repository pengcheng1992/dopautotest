# -*- coding:utf8 -*-
# Author:Pengcheng
from hujiang.pc.pageLib.dop.GetTime import GetTime


class AddStrtegy(object):
    strategy_manage = "//div/i[contains(@class,'fa fa-book')]/.."
    distribute = "//phx-sidenav-item[@ng-reflect-link='/strategy/send']"
    customer = "//label[text()='客户']/following-sibling::*//div"
    basic_customer = "//phx-select-option[text()='基础-测试客户']"
    user_crowd = "//label[text()='用户群']/following-sibling::*//div"
    basic_user_crowd = "//phx-select-option[text()='自动化导入人群——基础(10339)']"
    crowd = "//label[text()='人群']/following-sibling::*//div"
    import_crowd = "//phx-select-option[text()='导入人群']"
    new_strategy = "//button[contains(text(),'新增分发策略')]"

class NewDistribute(object):
    strategy_name = "//input[contains(@class,'form-control') and contains(@textreplaceregexp,'s')]"
    strategy_name_alert = "//div[contains(text(), '策略')]"
    strategy_crowd = "//label[contains(text(),'所属用户群')]/following-sibling::*/div"
    remarks = "//label[text()='备注']//following-sibling::*"
    user_percent = "//input[@formcontrolname = 'percentage']"
    push_frequency = "//label[text()=' 分发频率']//following-sibling::*/div"
    distribute_time = "//label[contains(text(),'分发时间')]/following-sibling::*/phx-select"
    every_day = "//*[contains(@id,'phx-select-option') and contains(text(),'"+str(GetTime().get_date_weekday())+"')]"
    every_month = "//*[contains(@id,'phx-select-option') and text()='"+str(GetTime().get_time_day())+"']"
    save_strategy = "//div[@class = 'form-group form-group-inline pt-3']/section/button[@class='btn btn-primary']"
    cancel = "//button[text()='取消']"
    distribute_list_chose = "//phx-table-cell[contains(text(),'小鹏导入人群测试8分发策略')]/preceding-sibling::*//div"
    distribute_status = "//phx-table-cell[contains(text(),'小鹏导入人群测试8分发策略')]/following-sibling::*//a/text()"
    file = "//button[text()='归档']"
    recovery = "//button[text()='恢复']"