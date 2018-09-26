# # -*- coding:utf8 -*-
# # Author:Pengcheng
#
# from hjAuto.ui.pc.common.CommonLib import puCom
# from hujiang.utilityBiz.pc.commonBiz import CommonBiz
#
#
#
# class DopLib(CommonBiz):
#
#     # 检验字段是否符合要求
#     # ispass:合法还是非法数值
#     # field：字段名
#     # fieldobj：字段xpath地址
#     # fielddata：预期提示字符串
#     #fieldmsg：预期提示字符串具体值
#
#     def verify_field(self,ispass,field,save,fieldobj=None,fielddata=None,fieldmsg=None,msg=None):
#         puCom.infoBold(msg)
#         if ispass==1:
#             if (puCom.element._is_visible(fieldobj)==False or fieldobj==None) and puCom.element._is_disabled(save)==False :
#                 puCom.infoBold(field+"字段校验通过，合法字段没有进行提示，并且可以进行保存")
#             else:
#                 puCom.error(field+"字段校验不通过，合法字段出现了提示，或者不能进行保存")
#
#         else:
#             if (puCom.element._is_visible(fieldobj) or fieldobj==None) and puCom.element._is_disabled(save):
#                 if fieldobj!=None and fielddata!=None and fieldmsg !=None:
#                     puCom.element.verify_element_text(fieldobj,fielddata[fieldmsg])
#                 puCom.infoBold(field+"字段校验通过，非法字段有提示，并且不能保存")
#             else:
#                 puCom.error(field+"字段校验不通过，非法字段没有出现提示，或者可以进行保存")
#
#
#     # 输入策略名称
#     # field：字段名
#     # fieldobj：输入框xpath地址
#     # fielddata：需要输入的值
#     def input_field(self,field,fieldobj=None,fielddata=None):
#         puCom.infoBold(field+"输入:"+fielddata)
#         puCom.input.set_value(fieldobj,fielddata)
#         puCom.element.click_if_exist("//div")
#
#     def enter_field(self,field,fieldobj,fieldata,save,verifyobj=None,verifydata=None,verifymsg=None):
#         for i in fieldata:
#             doplib.input_field(field, fieldobj,fieldata[i][0])
#             doplib.verify_field(fieldata[i][1], field, save,verifyobj,verifydata,verifymsg,"检验" + field + "是否能通过")
#
#
#
#     def continue_clicks(self,elementdatas,msg=None):
#         if len(elementdatas)>0 :
#             for i in elementdatas:
#                 puCom.infoBold("开始点击元素："+i)
#                 puCom.element.click_if_exist(i)
#         else:
#             puCom.infoBold("点击元素个数小于或者等于0个")
#
# doplib = DopLib()
