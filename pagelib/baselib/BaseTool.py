# -*- coding:utf8 -*-
# create by pengcheng

from selenium import webdriver
from conf.EnvConf import sysconf as sc
from conf.LogConf import  lc
from pagelib.baselib.GetTime import gt
from pagelib.baselib.OsPath import op
from pagelib.baselib.HtmlLogger import HTMLLogger


'''基础的工具类，主要针对浏览器的一些操作，打开浏览器、关闭浏览器、最大化、前进、后退、获取数据字典、截图等'''

class BaseTool(HTMLLogger):
    driver = None
    def open_browser(self,url,msg=None):
        self.info(msg)
        if  (sc.browser == "chrome"):
            # 打开谷歌浏览器
            try:
                self.driver = webdriver.Chrome()
                self.info("打开谷歌浏览器")
            except:
                self.error("打开谷歌浏览器失败")
        elif (sc.browser == "firefox"):
            # 打开火狐浏览器
            try:
                self.driver = webdriver.Firefox()
                self.info("打开火狐浏览器")
            except:
                self.error("打开火狐浏览器失败")
        elif (sc.browser == "ie"):
            # 打开IE浏览器
            try:
                self.driver = webdriver.Ie()
                self.info("打开IE浏览器")
            except:
                self.error("打开IE浏览器失败")
        else:
            self.error("不支持的浏览器")
        self.max_window()
        # 跳转到url
        self.get_url(url)


    # 窗口最大化
    def max_window(self):
        self.driver.maximize_window()
        self.info("窗口最大化")

    # 跳转到URL
    def get_url(self,url):
        try:
            self.driver.get(url)
            self.info("跳转到：【"+url+"】页面")
        except:
            self.error("跳转【"+url+"】失败，请检查URL是否正确！")

    # 关闭浏览器
    def close_browser(self):
        try:
            self.driver.close()
            self.info("成功关闭浏览器")
        except:
            self.error("关闭浏览器失败")

    # 获取网页截图
    def pic_shot(self):
        try:
            # 截图保存路径
            filepath =op.get_project_path()+"/"+lc.shot_path+str(gt.get_time_date())+"/"
            # 截图展示路径
            showpath = lc.shot_show_path+str(gt.get_time_date())+"/"
            self.debug("截图路径：【"+filepath+"】")
            op.path_exists_create(filepath)
            # 截图名字
            filename = gt.get_time_filename()+lc.shot_type
            self.debug("截图名字：【"+filename+"】")
            name = filepath+filename
            self.debug("截图完整路径+名字：【"+name+"】")
            # 进行截图操作
            self.driver.save_screenshot(name)
        except :
            self.error("截图失败")
        else:
            self.info("截图成功,截图存储路径为：【"+name+"】")
            self.info("picshot_1"+showpath+filename)

    # 获取字典数据
    def get_data(self,data_dict,env=None):
        # 根据环境取数据
        if env == None and sc.env in sc.envlist:
            try:
                value = data_dict.get(sc.env)
                self.debug("获取到的数据为：\n"+value)
                return value
            except:
                self.error("不支持的数据格式，请使用python字典格式！")
        elif env !=None and env in sc.envlist:
            try:
                value = data_dict.get(env)
                self.debug("获取到的数据为：\n" + value)
                return value
            except:
                self.error("不支持的数据格式，请使用python字典格式！")
        else:
            self.error("环境配置不正确，请检查环境配置，仅支持【qa】、【yz】、【prod】三种环境！")


bt = BaseTool()