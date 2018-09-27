

from pagelib.baselib.Element import pucom
from pagelib.caselib.LoginLib import login
from pagelib.caselib.NewStrategyLib import nsl

class TestCase1():

    def setUp(self):
        pucom.info("============test class setup==============")
        pucom.open_browser("http://qadop.hujiang.com/marketing/","打开浏览器并跳转到dop首页")
        login.logindop("step1:以用户名密码登录dop")
        login.verify_UserName("step2:检查是否登录成功")


    def teardown(self):
        pucom.info("============test class teardown==============")
        pucom.close_browser()



    def test_new_strategy(self):
        pucom.info()





