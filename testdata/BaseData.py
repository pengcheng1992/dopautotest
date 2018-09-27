# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.Element import pucom
from conf.EnvConf import sysconf as sc
class BaseData(object):

    def url(self):
        return pucom.get_data(
            {
                sc.qa:"http://qadop.hujiang.com/marketing",
                sc.yz:"http://yzdop.hujiang.com/marketing",
                sc.prod:"http://dop.hujiang.com/marketing"
            }
        )

class LoginData(object):
    def userinfo(self):
        return pucom.get_data(
            {
                sc.qa:{"username":"pengcheng2819","password":"pengcheng2819","realname":"彭成"} ,
                sc.yz: {"username":"pengcheng2819","password":"pengcheng2819","realname":"彭成"},
                sc.prod: {"username":"pengcheng2819","password":"pengcheng2819","realname":"彭成"}
            }
        )
bd = BaseData()
ld = LoginData()