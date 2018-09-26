# -*- coding:utf8 -*-
# create by pengcheng
from pagelib.baselib.GetTime import GetTime
class PushStrategyObj(object):
    new_strategy = "//button[contains(text(),'新增推送策略')]"   #新增推送策略按钮
    strategy_name = "//input[contains(@class,'form-control') and contains(@textreplaceregexp,'s')]"     #策略名称输入框
    strategy_name_alert = "//div[contains(text(), '策略未推送成功')]"      #过期时长备注解释
    strategy_crowd = "//label[contains(text(),'所属用户群')]/following-sibling::*/div"       #所属用户群下拉框
    remarks = "//label[text()='备注']//following-sibling::*"      #备注输入框
    user_percent = "//input[@formcontrolname = 'percentage']"       #分组比例输入框
    push_frequency = "//label[text()=' 推送频率']//following-sibling::*/div"        #推送频率下拉框
    save_strategy = "//div[@class = 'form-group form-group-inline pt-3']/section/button[@class='btn btn-primary']"      #保存按钮
    cancel = "//button[text()='取消']"        #取消按钮
    add_content = "//button[text()='新增内容']"     #新增内容按钮
    binding_content = "//button[text()='绑定内容']"     #绑定内容按钮
    lack_of_time_alert = "//phx-dialog-container"       #时间早于当前的警告弹框
    alert_information = "//phx-dialog-container//phx-dialog-content"        #时间早于当前的弹框提示信息
    alert_determine = "//button[text() = '确定']"     #弹框确定按钮
    alert_cancel = "//button[text() = '取消']"        #弹框取消按钮
    verify_strategy_success = "//a[text() = 'ceshicelve1']"
    verify_strategy_content_binding = "//span[contains(@class , 'text-danger') and contains(text(),'内容')]"
    verify_push_time = "//div[contains(@class,'alert-danger') and contains(text(),'日期')]"
    verify_percent = "//div[contains(@class , 'alert-danger') and contains(text(),'比例')]"
    verify_strategy_name = "//div[contains(@class , 'alert-danger') and contains(text(),'名称')]"
    content_id = "//div[contains(@class ,'phx-input phx-input-primary')]/label[contains(text(),'"
    binding_content_determine = "//button[text() = '确定']"
    cancel_binding = "//phx-table-cell[text()='630']/following-sibling::*//a[text() = '解绑']"
    onetime_push = "//label[contains(text(),'一次推送完成')]"
    setting_time = "//label[contains(text(),'设置时长')]"
    setting_time_hour = "//label[contains(text(),'设置时长')]/../following-sibling::*/phx-select[1]"
    # setting_hour = "//*[contains(@id,'phx-select-option') and text() = "+str(21-GetTime.get_time_hour())+"]"
    setting_time_minute = "//label[contains(text(),'设置时长')]/../following-sibling::*/phx-select[2]"
    setting_minute = "//*[@id='phx-select-option-162']"

class Everyday(object):
    every_day = "//phx-select-option[text()='每天']"

class Weekly(object):
    weekly = "//phx-select-option[text()='每周']"
    push_date = "//label[text()=' 推送时间']//following-sibling::*//span[text()='周一']"
    current_day = "//phx-select-option[text()='" + str(GetTime().get_date_weekday()) + "']"

class Monthly(object):
    monthly = "//phx-select-option[text()='每月']"
    push_date = "//label[text()=' 推送时间']//following-sibling::*//span[text()='1日']"
    current_day = "//phx-select-option[text()='" + str(GetTime().get_time_day()) + "日']"
    push_time = "//label[text()=' 推送时间']//following-sibling::*//span[text()='08']"
    current_time = "//phx-select-option[text()='" + str(GetTime().get_time_hour() - 1) + "']"
    push_minute = "//label[text()=' 推送时间']//following-sibling::*//span[text()='00']"
    thirty_minute = "//phx-select-option[text()='30']"

class Disposable(object):
    disposable = "//phx-select-option[text()='一次性']"
    push_date = "//label[text()=' 推送时间']//following-sibling::*//div[@class ='phx-datepicker-trigger-input']"
    push_year = "//div[@class ='phx-calendar-control-dropdown-content']/span[text()='" + str(
        GetTime().get_time_year()) + "']"
    push_month = "//div[@class ='phx-calendar-control-dropdown-content']/span[text()='" + str(
        GetTime().get_time_month()) + "']"
    date = "//div[@data = '" + str(GetTime().get_time_stamp()) + "']"
    year = "//div[contains(@class,'phx-calendar-control-dropdown-option') and contains(text(),' " + str(
        GetTime().get_time_year()) + "\n')]"
    month = "//div[contains(@class,'phx-calendar-control-dropdown-option') and contains(text(),' " + str(
        GetTime().get_time_month()) + "\n')]"
    push_year_verify = "//div[@class ='phx-calendar-control-dropdown-content']/span[text()='" + str(
        GetTime().get_time_year() + 1) + "']"

    # 点击确定按钮后修改时间

class Modify(object):
    modify_push_time = "//label[text()=' 推送时间']//following-sibling::*//span[text()='" + str(
        GetTime().get_time_hour() - 1) + "']"
    push_ok_time = "//phx-select-option[text()='" + str(GetTime().get_time_hour() + 1) + "']"
