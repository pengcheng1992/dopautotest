# -*- coding:utf8 -*-
# Author:Pengcheng


from conf.EnvConf import sysconf as sc
from pagelib.baselib.Element import pucom

class NewStrategyData(object):
    @property
    def strategynamedata(self):
        return pucom.get_data({
            sc.qa: {
                'name0': [' ',0],
                'name2': ['12',0],
                'name3': ['123',1],
                'name50':['   selecttd1.classid,sum(td1.1day),sum(td2.7day)froms   ',1],
                'name51':[ 'selecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0]
            },
            sc.yz: {
                'name0': [' ',0],
                'name2': ['12',0],
                'name3': ['123',1],
                'name50':['   selecttd1.classid,sum(td1.1day),sum(td2.7day)froms   ',1],
                'name51':[ 'selecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0]
            },
            sc.prod: {
                'name0': [' ',0],
                'name2': ['12',0],
                'name3': ['123',1],
                'name50':['   selecttd1.classid,sum(td1.1day),sum(td2.7day)froms   ',1],
                'name51':[ 'selecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0]
            }
        })



    @property
    def strategymemodata(self):
        return pucom.get_data({
            sc.qa: {
                'memo100': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms',1],
                'memo101': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0],
                'memo':['自动化测试增加策略',1]
            },
            sc.yz: {
                'memo100': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms',1],
                'memo101': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0],
                'memo':['自动化测试增加策略',1]
            },
            sc.prod: {
                'memo100': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms',1],
                'memo101': ['selecttd1.classid,sum(td1.1day),sum(td2.7day)fromsselecttd1.classid,sum(td1.1day),sum(td2.7day)froms1',0],
                'memo':['自动化测试增加策略',1]
            }
        })


    @property
    def strategypercentdata(self):
        return pucom.get_data({
            sc.qa: {
                'percent0': ['0',0],
                'percent100': ['100',1],
                'percent10.1': ['10.1',0],
                'percent101': ['101',0],
                'percentabc': ['abc',0]
            },
            sc.yz: {
                'percent0': ['0',0],
                'percent100': ['100',1],
                'percent10.1': ['10.1',0],
                'percent101': ['101',0],
                'percentabc': ['abc',0]
            },
            sc.prod: {
                'percent0': ['0',0],
                'percent100': ['100',1],
                'percent10.1': ['10.1',0],
                'percent101': ['101',0],
                'percentabc': ['abc',0]
            }
        })

    @property
    def strategypercentname(self):
        return pucom.get_data({
            sc.qa: {
                'percentname': '分组1'
            },
            sc.yz: {
                'percentname': '分组1'
            },
            sc.prod: {
                'percentname': '分组1'
            }
        })

    @property
    def strategypromptdata(self):
        return pucom.get_data({
            sc.qa: {
                'strategyname': '策略名称必填且长度为3～50个字符',
                'percent': '比例必须是在1%～100%之间的正整数',
                'pushtime': '指定日期不在有效期范围内',
                'binding': '内容条数超出限制（1条策略最多绑定1条短信、3种平台的App push、1条微信、1条邮件）'
            },
            sc.yz: {
                'strategyname': '策略名称必填且长度为3～50个字符',
                'percent': '比例必须是在1%～100%之间的正整数',
                'pushtime': '指定日期不在有效期范围内',
                'binding': '内容条数超出限制（1条策略最多绑定1条短信、3种平台的App push、1条微信、1条邮件）'
            },
            sc.prod: {
                'strategyname': '策略名称必填且长度为3～50个字符',
                'percent': '比例必须是在1%～100%之间的正整数',
                'pushtime': '指定日期不在有效期范围内',
                'binding': '内容条数超出限制（1条策略最多绑定1条短信、3种平台的App push、1条微信、1条邮件）'
            }
        })

    @property
    def strategybindingtdata(self):
        return pucom.get_data({
            sc.qa: {
                'duanxin1': '640',
                'duanxin2': '641',
                'weixin1': '642',
                'weixin2': '643',
                'ios1':'578',
                'ios2':'545',
                'android1':'576',
                'android2':'571',
                'xiaomi1':'572',
                'xiaomi2':'577',
                'email1':'580',
                'email2':'574'
            },
            sc.yz: {
                'duanxin1': '640',
                'duanxin2': '641',
                'weixin1': '642',
                'weixin2': '643',
                'ios1':'578',
                'ios2':'545',
                'android1':'576',
                'android2':'571',
                'xiaomi1':'572',
                'xiaomi2':'577',
                'email1':'580',
                'email2':'574'
            },
            sc.prod: {
                'duanxin1': '640',
                'duanxin2': '641',
                'weixin1': '642',
                'weixin2': '643',
                'ios1':'578',
                'ios2':'545',
                'android1':'576',
                'android2':'571',
                'xiaomi1':'572',
                'xiaomi2':'577',
                'email1':'580',
                'email2':'574'
            }
        })

newstrategydata = NewStrategyData()
