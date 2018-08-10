# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.BaseTool import bt
class BaseData(object):
    def url(self):
        return bt.get_data(
            {
                "qa":"http://qadop.hujiang.com/marketing",
                "yz":"http://yzdop.hujiang.com/marketing",
                "prod":"http://dop.hujiang.com/marketing"
            }
        )

bd = BaseData()