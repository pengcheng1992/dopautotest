# -*- coding:utf8 -*-
# create by pengcheng
import time
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
            except Exception:
                self.error(str(timeout)+"秒内根据name查找元素失败，请确认元素name是否正确：【" + name + "】")

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
                except Exception:
                    self.error("根据xpath查找元素失败，请确认元素xpath是否正确：【" + xpath + "】")
            else:
                self.error("根据xpath查找元素不存在，请确认元素xpath是否正确：【" + xpath + "】")

    #通过ID查找元素
    def find_element_byid(self,id,timeout=libc.timeout):
        if self.driver == None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            try:
                self.element = self.driver.find_element_by_id(id)
                self.info("根据id查找元素，元素id是：【" + id + "】")
                return self.element
            except Exception:
                self.error(str(timeout)+"秒内根据id查找元素失败，请确认元素id是否正确：【" + id + "】")

    #如果元素存在的话，点击元素
    def click_if_exist(self,xpath,timeout=libc.timeout):
        self.debug("如果元素存在则点击，地址：【"+xpath+"】")
        if self.driver == None:
            self.error("self.driver等于None,没有打开浏览器！")
        else:
            if self.is_exist(xpath) and self.is_enabled(xpath):
                if timeout!=libc.timeout:   #额外添加点击等待时间
                    time.sleep(timeout)
                self.driver.find_element_by_xpath(xpath).click()
                self.info("点击元素地址是：【" + xpath + "】")
            else:
                self.error("元素不可点击，地址：【"+xpath+"】")

    def is_visible(self, xpath, timeout=10):
        self.info( "判断元素是否显示：【"+ str(xpath) +"】")
        element = self.driver.find_element_by_xpath(xpath)
        if element is not None:
            try:
                displayed = element.is_displayed()
                self.info('元素地址：【"' + str(xpath) + '"】 is displayed: ' + str(displayed))
                return displayed
            except:
                return False
        return False


    #给输入框输入值
    def set_value(self,xpath,value,timeout=libc.timeout):
        self.debug("给输入框输入值，元素地址是：【" + xpath + "】"+"value:【"+value+"】")
        if self.is_exist(xpath,timeout) and self.is_enabled(xpath,timeout):
            try:
                self.driver.find_element_by_xpath(xpath).send_keys(value)
                self.info("给输入框输入值，输入框地址:【"+xpath+"】"+"，输入值为：【"+value+"】")
            except:
                self.error("给输入框输入值错误，请核对输入框地址【"+xpath+"】"+"，输入值为：【"+value+"】")
        else:
            self.error("元素不存在，请核对元素地址是否正确：【"+xpath+"】")

    #判断元素是否存在,不存在返回false，存在返回元素
    def is_exist(self,xpath,timeout=libc.timeout):
        self.debug("判断元素是否存在，元素地址是：【" + xpath + "】" )
        Timeout = None
        for Timeout in range(1,timeout):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                return element
            except Exception:
                self.error("查找元素超时【" + str(Timeout) + "】")
                time.sleep(1)
        if Timeout>=timeout-1:
            self.error("查找元素出错，请确认元素地址是否正确：【" + xpath + "】")
            self.pic_shot()
            return False

    def get_text(self,xpath,timeout=libc.timeout):
        self.debug("获取元素文本，元素地址：【"+xpath+"】")
        try:
            if self.is_exist(xpath,timeout):
                text = self.driver.find_element_by_xpath(xpath).text
                self.info("获取的文本为："+text)
                return text
            else:
                self.info("元素不存在，元素地址：【"+xpath+"】")
        except:
            self.error("获取元素文本失败，请确认地址正确：【"+xpath+"】")
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
            except Exception:
                self.error("等待元素启用失败【" + str(Timeout) + "】")
                time.sleep(1)
        if Timeout >= timeout - 1:
            self.error("元素为禁用状态：【" + xpath + "】")
            self.pic_shot()
            return False



pucom = Element()