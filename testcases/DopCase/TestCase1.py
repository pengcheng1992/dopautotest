

from pagelib.baselib.Element import pucom
from pagelib.caselib.LoginLib import login
from pagelib.caselib.NewStrategy import nsl

class TestCase1():

    def setUp(self):
        pucom.info("============test class setup==============")
        pucom.open_browser("http://qadop.hujiang.com/marketing/","打开浏览器并跳转到dop首页")
        login.logindop("step1:以用户名密码登录dop")
        login.verify_UserName("step2:检查是否登录成功")


    def teardown(self):
        pucom.close_browser()
        pucom.info("============test class teardown==============\n\n")


    def test001_new_evryday_strategy(self):
        nsl.new_name("step3:利用日期函数生成策略名称")
        nsl.select_condition("step4:下拉框选择客户人群以及用户群")
        nsl.enter_info("step5:进入新增页面并且输入信息")
        nsl.select_everyday("step6:选择新建每天类型的策略")
        nsl.click_save_button("step7:点击保存按钮")
        nsl.verify_alert_monthly("step8:检查推送时间为当前时间之前是否有弹框提醒")
        nsl.modify_push_time("step9:修改推送时间")
        nsl.click_save_button("step10:点击保存按钮")
        nsl.verify_addstrategy_success("step11:检查策略是否添加成功")

        # 添加每周策略
    def test002_new_weekday_strategy(self):
        nsl.new_name("step3:利用日期函数生成策略名称")
        nsl.select_condition("step4:下拉框选择客户人群以及用户群")
        nsl.enter_info("step5:进入新增页面并且输入信息")
        nsl.select_weekly("step6:选择新建每周类型的策略")
        nsl.click_save_button("step7:点击保存按钮")
        nsl.verify_alert_monthly("step8:检查推送时间为当前时间之前是否有弹框提醒")
        nsl.modify_push_time("step9:修改推送时间")
        nsl.click_save_button("step10:点击保存按钮")
        nsl.verify_addstrategy_success("step11:检查是否添加成功")

        # 添加每月策略
    def test003_new_monthly_strategy(self):
        nsl.new_name("step3:利用日期函数生成策略名称")
        nsl.select_condition("step4:下拉框选择客户人群以及用户群")
        nsl.enter_info("step5:进入新增页面并且输入信息")
        nsl.select_monthly("step6:选择新建每月类型的策略")
        nsl.click_save_button("step7:点击保存按钮")
        nsl.verify_alert_monthly("step8:检查推送时间为当前时间之前是否有弹框提醒")
        nsl.modify_push_time("step9:修改推送时间")
        nsl.click_save_button("step10:点击保存按钮")
        nsl.verify_addstrategy_success("step11:检查是否添加成功")

        #添加一次性策略
    def test004_new_disposable_strategy(self):
        nsl.new_name("step3:利用日期函数生成策略名称")
        nsl.select_condition("step4:下拉框选择客户人群以及用户群")
        nsl.enter_info("step5:进入新增页面并且输入信息")
        nsl.select_disposable("step6:选择新建一次性类型的策略")
        nsl.click_save_button("step7:点击保存按钮")
        nsl.verify_alert_disposable("step8:检查推送时间为当前时间之前是否有弹框提醒")
        nsl.modify_push_time("step9:修改推送时间")
        nsl.click_save_button("step10:点击保存按钮")
        nsl.verify_addstrategy_success("step11:检查是否添加成功")
