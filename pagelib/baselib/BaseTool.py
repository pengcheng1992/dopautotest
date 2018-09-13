# -*- coding:utf8 -*-
# create by pengcheng

from selenium import webdriver
<<<<<<< Updated upstream
from conf.EnvConf import sysconf as sc
from pagelib.baselib import Logger
import json
from pagelib.baselib.html_logger import setup,info,err,dbg,warn
=======
from conf.EnvConf import sysconf as sc,logconf as lc
from pagelib.baselib.HtmlLogger import info,err,dbg,warn,setup
>>>>>>> Stashed changes


class BaseTool(object):

    def __init__(self):
        setup(title=lc.title, version=lc.version, filename=lc.filename, mode=lc.mode, level=lc.level)
    driver = None
    def open_browser(self,url,msg=None):
        print(msg)
        if  (sc.browser == "chrome"):
            # 打开谷歌浏览器
            try:
                self.driver = webdriver.Chrome()
                info("打开谷歌浏览器")
            except:
                err("打开谷歌浏览器失败")
        elif (sc.browser == "firefox"):
            # 打开火狐浏览器
            try:
                self.driver = webdriver.Firefox()
                info("打开火狐浏览器")
            except:
                err("打开火狐浏览器失败")
        elif (sc.browser == "ie"):
            # 打开IE浏览器
            try:
                self.driver = webdriver.Ie()
                info("打开IE浏览器")
            except:
                err("打开IE浏览器失败")
        else:
            err("不支持的浏览器")


        # 窗口最大化
            self.driver.maximize_window();

        # 跳转到URL
        try:
            self.driver.get(url)
        except:
            print("跳转URL失败，请检查URL是否正确！")

    # 获取网页截图
    def pic_shot(self,filename):
        try:
            self.driver.save_screenshot(filename)
        except:
            err("截图失败")
<<<<<<< Updated upstream
=======
        else:
            info("截图成功")
            info('picshot_1'+filenameshot)
            info("截图完成")

>>>>>>> Stashed changes

    # 获取字典数据
    def get_data(self,data_dict,env=None):
        # 根据环境取数据
        if env == None and sc.env in sc.envlist:
            try:
                value = data_dict.get(sc.env)
                return value
            except:
                err("不支持的数据格式，请使用python字典格式！")
        elif env !=None and env in sc.envlist:
            try:
                value = data_dict.get(env)

                return value
            except:
                err("不支持的数据格式，请使用python字典格式！")
        else:
            err("环境配置不正确，请检查环境配置，仅支持【qa】、【yz】、【prod】三种环境！")




bt = BaseTool()