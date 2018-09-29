# -*- coding:utf8 -*-
# create by pengcheng
from pagelib.baselib.Element import pucom
from pagelib.baselib.GetTime import gt
from pagelib.caselib.DopLib import doplib
from pageobj.PushStrategyObj import pushstrategy as ps,Everyday,Monthly,Modify, Weekly, Disposable
from pageobj.HomeObj import homeobj
from testdata.NewStrategyData import newstrategydata as nsd
from nose.tools import *
class NewStrategy(object):
    name = ""
    # 生成策略名称
    def new_name(self, msg=None):
        pucom.info(msg)
        self.name = "自动化测试"+str(gt.get_date_time()).replace(" ","_")
        pucom.info("策略名称为：" + self.name)

    # 新增策略
    def select_condition(self, msg=None):
        pucom.info(msg)
        pucom.click_if_exist(homeobj.strategy_manage)
        pucom.click_if_exist(homeobj.push_strategy)
        pucom.click_if_exist(homeobj.customer)
        pucom.click_if_exist(homeobj.basic_customer)
        pucom.click_if_exist(homeobj.crowd)
        pucom.click_if_exist(homeobj.import_crowd)
        pucom.click_if_exist(homeobj.user_crowd)
        pucom.click_if_exist(homeobj.basic_user_crowd)

        # 点击新增策略并且输入合法信息
    def enter_info(self, msg=None):
        nameobj = ps.strategy_name #策略名称元素地址
        namedata = nsd.strategynamedata  #策略名称case数据
        vnameobj = ps.verify_strategy_name  #策略名称提示信息元素地址
        vnamedata = nsd.strategypromptdata  #策略名称预期提示内容

        percentname = ps.percent_name
        percentobj = ps.user_percent  #百分比元素地址
        percentdata = nsd.strategypercentdata  #百分比case数据
        vpercentobj = ps.verify_percent   #百分比提示信息元素地址
        vpercentdata = nsd.strategypromptdata  #百分比预期提示内容

        memoobj = ps.remarks
        memodata = nsd.strategymemodata

        save = ps.save_strategy  #保存按钮元素地址

        pucom.info(msg)
        pucom.click_if_exist(ps.new_strategy)
        pucom.set_value(ps.strategy_name, self.name)
        pucom.set_value(memoobj, memodata['memo'][0])
        pucom.set_value(percentobj, percentdata['percent100'][0])
        pucom.set_value(percentname,nsd.strategypercentname['percentname'])
        # 开始输入框正反用例校验
        pucom.info("开始输入框正反用例校验")
        doplib.enter_field("策略名称", nameobj,namedata ,save,vnameobj,vnamedata ,"strategyname")
        pucom.set_value(nameobj, self.name)
        doplib.enter_field("备注",memoobj,memodata,save)
        pucom.set_value(memoobj, memodata['memo'][0])
        doplib.enter_field("用户分组比例",percentobj,percentdata,save,vpercentobj,vpercentdata,"percent")
        pucom.set_value(percentobj, percentdata["percent100"][0])
        pucom.click_if_exist(ps.push_frequency)

    # 选择每天策略
    def select_everyday(self, msg=None):
        pucom.info(msg)
        clicksdatas = [Everyday.every_day, Monthly.push_time, Monthly.current_time, Monthly.push_minute,
                       Monthly.thirty_minute]
        pucom.continue_clicks(clicksdatas)

    # 选择每周策略
    def select_weekly(self, msg=None):
        pucom.info(msg)
        clicksdatas = [Weekly.weekly, Weekly.push_date, Weekly.current_day, Monthly.push_time, Monthly.current_time,
                       Monthly.push_minute, Monthly.thirty_minute]
        pucom.continue_clicks(clicksdatas)


    # 选择每月策
    def select_monthly(self, msg=None):
        pucom.info(msg)
        clicksdatas = [Monthly.monthly, Monthly.push_date, Monthly.current_day, Monthly.push_time,
                       Monthly.current_time, Monthly.push_minute, Monthly.thirty_minute]
        pucom.continue_clicks(clicksdatas)

    # 选择一次性策略
    def select_disposable(self, msg=None):
        pucom.info(msg)
        clicksdatas = [Disposable.disposable, Disposable.push_date]
        pucom.continue_clicks(clicksdatas)
        # 操作日历控件
        clicksdatas = [Disposable.push_year,Disposable.year,Disposable.push_month,Disposable.month,Disposable.date]
        pucom.continue_clicks(clicksdatas)
        pucom.click_if_exist("//div")
        # 选择时间
        clicksdatas = [Monthly.push_time,Monthly.current_time,Monthly.push_minute,Monthly.thirty_minute]
        pucom.continue_clicks(clicksdatas)
        # 判断每月策略推送时间在现在之前是否有弹框提示
    def verify_alert_monthly(self, msg=None):
        pucom.info(msg)
        assert_true(pucom.is_visible(ps.lack_of_time_alert),"没有弹框，校验失败")
        pucom.info("有弹框，弹框校验正确")
        pucom.click_if_exist(ps.alert_cancel)

        # 判断一次性策略推送时间距离现在不足1.5小时是否有弹框提示
    def verify_alert_disposable(self, msg=None):
        pucom.info(msg)
        assert_true(pucom.is_visible(ps.lack_of_time_alert), "没有弹框，校验失败")
        pucom.info("有弹框，弹框校验正确")
        pucom.click_if_exist(ps.alert_cancel)

    # 修改时间
    def modify_push_time(self, msg=None):
        pucom.info(msg)
        clicksdatas = [Modify.modify_push_time, Modify.push_ok_time]
        pucom.continue_clicks(clicksdatas)


            # 点击保存按钮
    def click_save_button(self, msg=None):
        pucom.info(msg)
        pucom.click_if_exist(ps.save_strategy)

        # 检验策略是否添加成功
    def verify_addstrategy_success(self, msg=None):
        pucom.info(msg)
        if pucom.is_exist("//a[text() = '" + self.name + "']") and pucom.is_visible("//a[text() = '" + self.name + "']"):
            pucom.info("策略添加成功！")
        else:
            pucom.info("找不到添加的策略，策略添加失败!")
            assert_true(False,"策略添加失败")

nsl = NewStrategy()