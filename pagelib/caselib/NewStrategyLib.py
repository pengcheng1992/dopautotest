# # -*- coding:utf8 -*-
# # Author:Pengcheng
# from pagelib.baselib.Element import Element
# from pageobj.PushStrategyObj import Monthly, Disposable, Modify,Weekly,Everyday,PushStrategyObj
#
# from pagelib.baselib.GetTime import GetTime
#
#
# class NewStrategyLib(CommonBiz):
#     name = ""
#
#
#     # 生成策略名称
#     def new_name(self, msg=None):
#         puCom.infoBold(msg)
#         NewStrategyLib.name = "自动化测试"+str(GetTime().get_date_time()).replace(" ","_")
#         puCom.infoBold("策略名称为：" + NewStrategyLib.name)
#
#     # 新增策略
#     def select_condition(self, msg=None):
#         puCom.infoBold(msg)
#         puCom.element.click_if_exist(AddStrategy.strategy_manage)
#         puCom.element.click_if_exist(AddStrategy.push_strategy)
#         puCom.element.click_if_exist(AddStrategy.customer)
#         puCom.element.click_if_exist(AddStrategy.basic_customer)
#         puCom.element.click_if_exist(AddStrategy.crowd)
#         puCom.element.click_if_exist(AddStrategy.import_crowd)
#         puCom.element.click_if_exist(AddStrategy.user_crowd)
#         puCom.element.click_if_exist(AddStrategy.basic_user_crowd)
#
#         # 点击新增策略并且输入合法信息
#     def enter_info(self, msg=None):
#         nameobj = New_strategy.strategy_name #策略名称元素地址
#         namedata = newstrategydata.strategynamedata  #策略名称case数据
#         vnameobj = New_strategy.verify_strategy_name  #策略名称提示信息元素地址
#         vnamedata = newstrategydata.strategypromptdata  #策略名称预期提示内容
#
#         percentobj = New_strategy.user_percent  #百分比元素地址
#         percentdata = newstrategydata.strategypercentdata  #百分比case数据
#         vpercentobj = New_strategy.verify_percent   #百分比提示信息元素地址
#         vpercentdata = newstrategydata.strategypromptdata  #百分比预期提示内容
#
#         memoobj = New_strategy.remarks
#         memodata = newstrategydata.strategymemodata
#
#         save = New_strategy.save_strategy  #保存按钮元素地址
#
#         puCom.infoBold(msg)
#         puCom.element.click_if_exist(AddStrategy.new_strategy)
#         puCom.input.set_value(New_strategy.strategy_name, NewStrategyLib.name)
#         puCom.input.set_value(memoobj, memodata['memo'][0])
#         puCom.input.set_value(percentobj, percentdata['percent100'][0])
#         # 开始输入框正反用例校验
#         puCom.infoBold("开始输入框正反用例校验")
#         doplib.enter_field("策略名称", nameobj,namedata ,save,vnameobj,vnamedata ,"strategyname")
#         puCom.input.set_value(nameobj, NewStrategyLib.name)
#         doplib.enter_field("备注",memoobj,memodata,save)
#         puCom.input.set_value(memoobj, memodata['memo'][0])
#         doplib.enter_field("用户分组比例",percentobj,percentdata,save,vpercentobj,vpercentdata,"percent")
#         puCom.input.set_value(percentobj, percentdata["percent100"][0])
#         puCom.element.click_if_exist(New_strategy.push_frequency)
#
#         # 选择每天策略
#     def select_everyday(self, msg=None):
#         puCom.infoBold(msg)
#         clicksdatas = [Everyday.every_day,Monthly.push_time,Monthly.current_time,Monthly.push_minute,Monthly.thirty_minute]
#         doplib.continue_clicks(clicksdatas)
#
#
#         # 选择每周策略
#     def select_weekly(self, msg=None):
#         puCom.infoBold(msg)
#         clicksdatas = [Weekly.weekly,Weekly.push_date,Weekly.current_day,Monthly.push_time,Monthly.current_time,Monthly.push_minute,Monthly.thirty_minute]
#         doplib.continue_clicks(clicksdatas)
#
#
#         # 选择每月策略
#     def select_monthly(self, msg=None):
#         puCom.infoBold(msg)
#         clicksdatas = [Monthly.monthly,Monthly.push_date,Monthly.current_day,Monthly.push_time,Monthly.current_time,Monthly.push_minute,Monthly.thirty_minute]
#         doplib.continue_clicks(clicksdatas)
#
#
#         # 判断每月策略推送时间距离现在不足1.5小时是否有弹框提示
#     def verify_alert_monthly(self, msg=None):
#         puCom.infoBold(msg)
#         if puCom.element._is_visible(New_strategy.lack_of_time_alert):
#             puCom.infoBold("有弹框，弹框校验正确")
#             puCom.element.click_if_exist(New_strategy.alert_cancel)
#         else:
#             puCom.infoBold("没有弹框，校验失败！")
#             raise RuntimeError('没有弹框，校验失败！')
#
#         # 修改时间
#     def modify_push_time(self, msg=None):
#         puCom.infoBold(msg)
#         clicksdatas = [Modify.modify_push_time,Modify.push_ok_time]
#         doplib.continue_clicks(clicksdatas)
#
#         # 选择一次性策略
#     def select_disposable(self, msg=None):
#         puCom.infoBold(msg)
#         clicksdatas = [Disposable.disposable,Disposable.push_date]
#         doplib.continue_clicks(clicksdatas)
#
#         # 操作日历控件
#         clicksdatas = [Disposable.push_year,Disposable.year,Disposable.push_month,Disposable.month,Disposable.date]
#         doplib.continue_clicks(clicksdatas)
#         puCom.infoBold(Disposable.date)
#         # 选择时间
#         clicksdatas = [Monthly.push_time,Monthly.current_time,Monthly.push_minute,Monthly.thirty_minute]
#         doplib.continue_clicks(clicksdatas)
#
#
#         # 判断一次性策略推送时间距离现在不足1.5小时是否有弹框提示
#     def verify_alert_disposable(self, msg=None):
#         puCom.infoBold(msg)
#         if puCom.element._is_visible(New_strategy.lack_of_time_alert):
#             puCom.infoBold("有弹框，弹框校验正确")
#             puCom.element.click_if_exist(New_strategy.alert_determine)
#         else:
#             puCom.infoBold("没有弹框，校验失败！")
#             raise RuntimeError('没有弹框，校验失败！')
#
#
#         # 绑定内容
#     def binding_content(self,msg=None):
#         puCom.infoBold(msg)
#         puCom.element.click_if_exist(New_strategy.binding_content)
#         # puCom.element.click_if_exist(New_strategy.content_id + newstrategydata.strategybindingtdata['duanxin1'] + "')]")
#         puCom.checkbox._check_item(New_strategy.content_id + newstrategydata.strategybindingtdata['duanxin1'] + "')]","checked")
#         puCom.element.click_if_exist(New_strategy.binding_content_determine)
#
#
#
#         # 点击保存按钮
#     def click_save_button(self, msg=None):
#         puCom.infoBold(msg)
#         puCom.element.click_if_exist(New_strategy.save_strategy)
#
#         # 检验策略是否添加成功
#     def verify_addstrategy_success(self, msg=None):
#         puCom.infoBold(msg)
#         if puCom.element._is_visible("//a[text() = '" + NewStrategyLib.name + "']"):
#             puCom.element.verify_element_exist("//a[text() = '" + NewStrategyLib.name + "']")
#             puCom.infoBold("策略添加成功！")
#         else:
#             puCom.infoBold("找不到添加的策略，策略添加失败!")
#             raise RuntimeError("策略添加失败")
#
#
# newstrategylib = NewStrategyLib()
