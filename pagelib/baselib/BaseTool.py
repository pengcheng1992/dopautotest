# -*- coding:utf8 -*-
# create by pengcheng

from selenium import webdriver
from conf.EnvConf import sysconf as sc
from pagelib.baselib import Logger
import json



class BaseTool(object):

    def open_browser(self,url,msg=None):
        print(msg)
        if  (sc.browser == "chrome"):
            # 打开谷歌浏览器
            driver = webdriver.Chrome()
        elif (sc.browser == "firefox"):
            # 打开火狐浏览器
            driver = webdriver.Firefox()
        elif (sc.browser == "ie"):
            # 打开IE浏览器
            driver = webdriver.Ie()
        else:
            raise "不支持的浏览器！"

        # 窗口最大化
        driver.maximize_window();


        # 跳转到URL
        try:
            driver.get(url)

        except:
            print("跳转URL失败，请检查URL是否正确！")

    # 获取字典数据
    def get_data(self,data_dict,env=None):
        # 根据环境取数据
        if env == None and sc.env in sc.envlist:
            try:
                value = data_dict.get(sc.env)
                print(value)
                return value
            except:
                print("不支持的数据格式，请使用python字典格式！")
        elif env !=None and env in sc.envlist:
            try:
                value = data_dict.get(env)

                return value
            except:
                print("不支持的数据格式，请使用python字典格式！")
        else:
            raise  "环境配置不正确，请检查环境配置，仅支持【qa】、【yz】、【prod】三种环境！"




bt = BaseTool()