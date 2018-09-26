

from pagelib.baselib.Element import pucom
from pagelib.caselib.LoginLib import login

class TestCase1():

    def setUp(self):
        print("============test class setup==============")
        pucom.open_browser("http://qadop.hujiang.com/marketing/","打开DOP")


    def teardown(self):
        print("============test class teardown==============")
        pucom.close_browser()



    def test_new_strategy(self):
        login.logindop()



