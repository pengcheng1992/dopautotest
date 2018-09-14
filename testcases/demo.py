# -*- coding:utf8 -*-
# create by pengcheng

from pagelib.baselib.BaseTool import bt

class Demo(object):

    bt.open_browser("https://www.360.cn/","打开360首页！")
    bt.pic_shot()
    bt.close_browser()

    # bt.info("alsdfasdfja")
    # bt.err("alsdfasdfja")
    # bt.warn("alsdfasdfja")
    # bt.info("alsdfasdfja")
    # bt.info("中文测试")
    # bt.info("picshot_tulip.jpg")
    # bt.info("picshot_tulip11.jpg")




