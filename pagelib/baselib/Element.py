# -*- coding:utf8 -*-
# create by pengcheng
import time
from pagelib.baselib.HtmlLogger import log
from pagelib.baselib.BaseTool import BaseTool
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
'''
元素的基本操作，查找元素，操作元素等
'''
class Element(BaseTool):
    # 根据name查找元素
    element = None

    def find_element_byname(self,name,timeout=10):
        if self.driver ==None:
            log.error("self.driver等于None,没有打开浏览器！")
        else:
            try:
                self.element = self.driver.find_element_by_name(name)
                return self.element
            except Exception:
                log.error(timeout+"秒内根据name查找元素失败，请确认元素name是否正确：【" + name + "】")

    #通过xpath查找元素
    def find_element_byxpath(self,xpath,timeout=10):
        if self.driver ==None:
            log.error("self.driver等于None,没有打开浏览器！")
        else:
            if self.is_exist(xpath,timeout):
                try:
                    self.element = self.driver.find_element_by_xpath(xpath)
                    return self.element
                except Exception:
                    log.error("根据xpath查找元素失败，请确认元素xpath是否正确：【" + xpath + "】")
            else:
                log.error("根据xpath查找元素不存在，请确认元素xpath是否正确：【" + xpath + "】")

    #通过ID查找元素
    def find_element_byid(self,id,timeout=10):
        if self.driver == None:
            log.error("self.driver等于None,没有打开浏览器！")
        else:
            try:
                self.element = self.driver.find_element_by_id(id)
                return self.element
            except Exception:
                log.error(timeout+"秒内根据id查找元素失败，请确认元素id是否正确：【" + id + "】")

    #如果元素存在的话，点击元素
    def click_if_exist(self,xpath,timeout=5):
        log.debug("元素地址是：【" + xpath + "】")
        log.error(str(self.driver))
        if self.driver == None:
            log.error("self.driver等于None,没有打开浏览器！")
        else:
            if self.is_exist(xpath,timeout):
                self.driver.find_element_by_xpath(xpath).click()
            else:
                log.error("元素不存在，请核对元素地址是否正确：【"+xpath+"】")

    #给输入框输入值
    def set_value(self,xpath,value,timeout=5):
        log.debug("元素地址是：【" + xpath + "】"+"value:【"+value+"】")
        if self.is_exist(xpath,timeout):
            try:
                self.driver.find_element_by_xpath(xpath).send_keys(value)
            except:
                log.error("给输入框输入值错误，请核对输入框地址【"+xpath+"】"+"，输入值为：【"+value+"】")
        else:
            log.error("元素不存在，请核对元素地址是否正确：【"+xpath+"】")

    #判断元素是否存在
    def is_exist(self,xpath,timeout=10):
        log.debug("元素地址是：【" + xpath + "】" )
        Timeout = None
        for Timeout in range(1,timeout):
            try:
                self.driver.find_element_by_xpath(xpath)
                return True
            except Exception:
                log.error("查找元素超时【" + Timeout + "】")
                time.sleep(1)
        if Timeout>=timeout-1:
            log.error("查找元素出错，请确认元素地址是否正确：【" + xpath + "】")
            return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self,xpath,by=By.XPATH,timeout=10):
        log.debug("元素地址是：【" + xpath + "】")
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            log.error(timeout + "秒内根据【"+by+"】显示元素超时，请确认地址正确：【"+xpath+"】")
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self,xpath,by=By.XPATH,timeout=10):
        log.debug("元素地址是：【" + xpath + "】")
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((by, xpath)))
            return True
        except TimeoutException:
            log.error(timeout + "秒内元素隐藏超时，请确认地址正确：【" + xpath + "】")
            return False

pucom = Element()