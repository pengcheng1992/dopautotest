# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.BaseTool import bt,log
from pagelib.baselib.OsPath import op

class demo(object):
    bt.open_browser("http://www.hujiang.com","打开沪江首页")
    bt.pic_shot()
    bt.close_browser()