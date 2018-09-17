from nose.plugins.attrib import attr
from pagelib.baselib.BaseTool import bt,log

class TestCase1():

    def setUp(self):
        print("============test class setup==============")
        bt.open_browser("http://www.hujiang.com","打开沪江首页")

    def teardown(self):
        print("============test class teardown==============")
        bt.close_browser()


    def test_xxx(self):
        print("test_xxx")
        bt.pic_shot()

    def test_kkk(self):
        print("test_kkk")
        bt.pic_shot()
