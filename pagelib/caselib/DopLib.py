# -*- coding:utf8 -*-
# Author:Pengcheng

from pagelib.baselib.Element import pucom
from nose.tools import *
class DopLib(object):

    # 检验字段是否符合要求
    # ispass:合法还是非法数值
    # field：字段名
    # fieldobj：字段xpath地址
    # fielddata：预期提示字符串
    #fieldmsg：预期提示字符串具体值

    def verify_field(self,ispass,field,save,fieldobj=None,fielddata=None,fieldmsg=None,msg=None):
        pucom.info(msg)
        if ispass==1:
            if (fieldobj==None or pucom.is_visible(fieldobj)==False) and pucom.is_disabled(save)==False :
                pucom.info(field+"字段校验通过，合法字段没有进行提示，并且可以进行保存")
            else:
                pucom.error(field + "字段校验不通过，合法字段出现了提示，或者不能进行保存")
                assert_is_none(None,field+"字段校验不通过，合法字段出现了提示，或者不能进行保存")

        else:
            if (fieldobj==None or pucom.is_visible(fieldobj)) and pucom.is_disabled(save):
                if fieldobj!=None and fielddata!=None and fieldmsg !=None:
                    assert_equal(pucom.get_text(fieldobj),fielddata[fieldmsg],field+"字段校验不通过，非法字段没有出现提示，或者可以进行保存")
                pucom.info(field+"字段校验通过，非法字段有提示，并且不能保存")



    # 输入策略名称
    # field：字段名
    # fieldobj：输入框xpath地址
    # fielddata：需要输入的值
    def input_field(self,field,fieldobj=None,fielddata=None):
        pucom.info(field+"输入:"+fielddata)
        pucom.set_value(fieldobj,fielddata)
        pucom.click_if_exist("//div")

    def enter_field(self,field,fieldobj,fieldata,save,verifyobj=None,verifydata=None,verifymsg=None):
        for i in fieldata:
            doplib.input_field(field, fieldobj,fieldata[i][0])
            doplib.verify_field(fieldata[i][1], field, save,verifyobj,verifydata,verifymsg,"检验" + field + "是否能通过")





doplib = DopLib()
