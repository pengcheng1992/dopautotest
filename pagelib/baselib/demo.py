# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.BaseTool import bt
class demo(object):
    bt.open_browser("http://www.baidu.com","打开百度首页")
    bt.pic_shot()
    bt.close_browser()


