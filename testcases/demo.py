# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.BaseTool import bt
from testdata.BaseData import bd
class Demo(object):

    bt.open_browser(bd.url(),"打开dop首页！")