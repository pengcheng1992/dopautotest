# -*- coding:utf8 -*-
# create by pengcheng
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from pagelib.baselib.BaseTool import BaseTool
from conf.LibCof import libc


'''
元素的基本操作，查找元素，操作元素等
'''
class Element(BaseTool):
    # 根据name查找元素
    element = None
    def find_element_byname(self,name,timeout=libc.timeout):
        if self.driver ==None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            try:
                self.element = self.driver.find_element_by_name(name)
                self.info("根据name查找元素，元素name是：【" + name + "】")
                return self.element
            except Exception as e:
                self.error(str(timeout)+"秒内根据name查找元素失败，请确认元素name是否正确：【" + name + "】")
            self.error(" Exception:" + str(e))

    #通过xpath查找元素
    def find_element_byxpath(self,xpath,timeout=libc.timeout):
        if self.driver ==None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            if self.is_exist(xpath,timeout):
                try:
                    self.element = self.driver.find_element_by_xpath(xpath)
                    self.info("根据xpath查找元素，元素xpath是：【" + xpath + "】")
                    return self.element
                except Exception as e:
                    self.error("根据xpath查找元素失败，请确认元素xpath是否正确：【" + xpath + "】")
                    self.error(" Exception:" + str(e))
            else:
                self.error("根据xpath查找元素不存在，请确认元素xpath是否正确：【" + xpath + "】")
                return None

    #通过ID查找元素
    def find_element_byid(self,id,timeout=libc.timeout):
        if self.driver == None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            try:
                self.element = self.driver.find_element_by_id(id)
                self.info("根据id查找元素，元素id是：【" + id + "】")
                return self.element
            except Exception as e:
                self.error(str(timeout)+"秒内根据id查找元素失败，请确认元素id是否正确：【" + id + "】")
                self.error(" Exception:" + str(e))

    #如果元素存在的话，点击元素
    def click_if_exist(self,xpath,timeout=libc.timeout):
        self.info("如果元素存在则点击，地址：【"+xpath+"】")
        if self.driver == None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            if self.is_exist(xpath,timeout)  :
                try:
                    time.sleep(libc.clicktime)
                    self.debug("点击前休眠："+str(libc.clicktime)+"秒")
                    self.driver.find_element_by_xpath(xpath).click()
                    self.info("点击元素地址是：【" + xpath + "】")
                except Exception as e:
                    if "is not clickable at point" in repr(e):  # 判断元素是否有Action遮挡
                        element = self.driver.find_element_by_xpath(xpath)
                        actions = ActionChains(self.driver)
                        actions.move_to_element(element).click().perform()
                    else:
                        self.error("点击元素失败：【"+xpath+"】")
                        self.error(" Exception:" + str(e))
            else:
                self.error("元素不可点击，地址：【"+xpath+"】")

    #连续点击多个元素
    def continue_clicks(self,elementdatas,msg=None):
        self.info(msg)
        if len(elementdatas)>0 :
            for i in elementdatas:
                self.info("开始点击元素："+i)
                self.debug("元素地址为：【"+i+"】")
                self.click_if_exist(i)
        else:
            self.info("点击元素个数小于或者等于0个")

    #判断元素是否显示，显示为true，未显示为false
    def is_visible(self, xpath):
        self.info( "判断元素是否显示：【"+ str(xpath) +"】")
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if element is not None:
                displayed = element.is_displayed()
                self.info('元素地址：【"' + str(xpath) + '"】 is displayed: ' + str(displayed))
                return displayed
        except Exception as e:
            self.info("元素不显示：【"+xpath+"】")
            self.debug(str(e))
            return False

    #给输入框输入值
    def set_value(self,xpath,value,timeout=libc.timeout):
        self.debug("给输入框输入值，元素地址是：【" + xpath + "】"+"value:【"+value+"】")
        if self.is_exist(xpath,timeout) and self.is_enabled(xpath,timeout):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys(value)
                self.info("给输入框输入值，输入框地址:【"+xpath+"】"+"，输入值为：【"+value+"】")
            except Exception as e:
                self.error("给输入框输入值错误，请核对输入框地址【"+xpath+"】"+"，输入值为：【"+value+"】")
                self.debug(" Exception:"+str(e))
        else:
            self.error("元素不存在，请核对元素地址是否正确：【"+xpath+"】")

    #判断元素是否存在,不存在返回false，存在返回元素
    def is_exist(self,xpath,timeout=libc.timeout):
        self.debug("判断元素是否存在，元素地址是：【" + xpath + "】" )
        Timeout = None
        for Timeout in range(1,timeout):
            element = None
            try:
                element = self.driver.find_element_by_xpath(xpath)
                if element is None:
                    time.sleep(1)
                    continue
                if not isinstance(element, WebElement):
                    if str(Exception).lower().find("alert") != -1:
                        self.info("跳转到弹框")
                        self.driver.switch_to.alert.dismiss()
                        try:
                            element = self.driver.find_element_by_xpath(xpath)
                            return element
                        except:
                            time.sleep(1)
                            continue
                else:
                    return element
            except Exception as e:
                self.error("查找元素超时【" + str(Timeout) + "】")
                self.debug(" Exception:" + str(e))
                time.sleep(1)
        if Timeout>=timeout-1:
            self.error("查找元素出错，请确认元素地址是否正确：【" + xpath + "】")
            self.pic_shot()
            return False

    #获取元素文本信息
    def get_text(self,xpath,timeout=libc.timeout):
        self.debug("获取元素文本，元素地址：【"+xpath+"】")
        try:
            if self.is_exist(xpath,timeout):
                text = self.driver.find_element_by_xpath(xpath).text
                self.info("获取的文本为："+text)
                return text
            else:
                self.info("元素不存在，元素地址：【"+xpath+"】")
        except  Exception as e :
            self.error("获取元素文本失败，请确认地址正确：【"+xpath+"】")
            self.error(" Exception:" + str(e))
            return False

    # 一直等待某元素未置灰，默认超时10秒
    def is_enabled(self,xpath,timeout=libc.timeout):
        self.debug("等待元素启用，元素地址是：【" + xpath + "】")
        Timeout = None
        for Timeout in range(1, timeout):
            try:
                enabled = self.driver.find_element_by_xpath(xpath).is_enabled()
                self.debug("判断是否为可用:" + str(enabled))
                if enabled:
                    return True
            except Exception as e:
                self.error("等待元素启用失败【" + str(Timeout) + "】")
                self.error(" Exception:" + str(e))
                time.sleep(1)
        if Timeout >= timeout - 1:
            self.error("元素为禁用状态：【" + xpath + "】")
            self.pic_shot()
            return False

    #判断元素是否置灰
    def is_disabled(self, xpath):
        self.info("判断元素是否disabled： 【" + str(xpath) + "】")
        obj = self.driver.find_element_by_xpath(xpath)
        if obj is not None:
            status = str(obj.get_attribute("disabled")).lower()
            if status == "true" or status == "disabled":
                return True
            else:
                return False
        else:
            self.error("不能找到该元素：【'" + str(xpath) + "】")
            return False


pucom = Element()