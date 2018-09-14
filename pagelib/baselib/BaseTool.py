# -*- coding:utf8 -*-
# create by pengcheng

from selenium import webdriver
from conf.EnvConf import sysconf as sc
from conf.LogConf import  lc
from pagelib.baselib.GetTime import gt
from pagelib.baselib.OsPath import op
from pagelib.baselib.HtmlLogger import log


'''基础的工具类，主要针对浏览器的一些操作，打开浏览器、关闭浏览器、最大化、前进、后退、获取数据字典、截图等'''

class BaseTool(object):

    driver = None
    def open_browser(self,url,msg=None):
        log.info(msg)
        if  (sc.browser == "chrome"):
            # 打开谷歌浏览器
            try:
                self.driver = webdriver.Chrome()
                log.info("打开谷歌浏览器")
            except:
                log.error("打开谷歌浏览器失败")
        elif (sc.browser == "firefox"):
            # 打开火狐浏览器
            try:
                self.driver = webdriver.Firefox()
                log.info("打开火狐浏览器")
            except:
                log.error("打开火狐浏览器失败")
        elif (sc.browser == "ie"):
            # 打开IE浏览器
            try:
                self.driver = webdriver.Ie()
                log.info("打开IE浏览器")
            except:
                log.error("打开IE浏览器失败")
        else:
            log.error("不支持的浏览器")
        # 跳转到url
        self.get_url(url)
        self.max_window()

    # 窗口最大化
    def max_window(self):
        self.driver.maximize_window();
        log.info("窗口最大化")

    # 跳转到URL
    def get_url(self,url):
        try:
            self.driver.get(url)
            log.info("跳转到：【"+url+"】页面")
        except:
            log.error("跳转【"+url+"】失败，请检查URL是否正确！")

    # 关闭浏览器
    def close_browser(self):
        try:
            self.driver.close()
            log.info("成功关闭浏览器")
        except:
            log.error("关闭浏览器失败")

    # 获取网页截图
    def pic_shot(self):
        try:
            # 截图保存路径
            filepath ="../../"+lc.shot_path+str(gt.get_time_date())+"/"
            log.debug("截图路径：【"+filepath+"】")
            op.path_exists_create(filepath)
            # 截图名字
            filename = gt.get_time_filename()+lc.shot_type
            log.debug("截图名字：【"+filename+"】")
            name = filepath+filename
            log.debug("截图完整路径+名字：【"+name+"】")
            # 进行截图操作
            self.driver.save_screenshot(name)
        except :
            log.error("截图失败")
        else:
            log.info("截图成功,截图存储路径为：【"+name+"】")
            log.info("picshot_1"+name)

    # 获取字典数据
    def get_data(self,data_dict,env=None):
        # 根据环境取数据
        if env == None and sc.env in sc.envlist:
            try:
                value = data_dict.get(sc.env)
                log.debug("获取到的数据为：\n"+value)
                return value
            except:
                log.error("不支持的数据格式，请使用python字典格式！")
        elif env !=None and env in sc.envlist:
            try:
                value = data_dict.get(env)
                log.debug("获取到的数据为：\n" + value)
                return value
            except:
                log.error("不支持的数据格式，请使用python字典格式！")
        else:
            log.error("环境配置不正确，请检查环境配置，仅支持【qa】、【yz】、【prod】三种环境！")


bt = BaseTool()