# -*- coding:utf8 -*-
# creat by pengcheng

from selenium import webdriver
from conf.envconf import sysconf

class BT(object):
    def open_browser(self,url,msg=None):
        print(msg)
        if  (sysconf.browser == "chrome"):
            driver = webdriver.Chrome()
        elif (sysconf.browser == "firefox"):
            driver = webdriver.Firefox()
        elif (sysconf.browser == "ie"):
            driver = webdriver.Ie()
        else:
            raise "不支持的浏览器！"
        driver.get(url)
        driver.maximize_window();

bt = BT()