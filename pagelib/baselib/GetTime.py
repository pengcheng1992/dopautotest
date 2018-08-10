# -*- coding:utf8 -*-
# create by pengcheng
import time
import datetime


class GetTime(object):

    # 获取当天凌晨的时间戳
    def get_time_stamp(self):
        t = time.localtime(time.time())
        return time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S')) * 1000
    # 获取当前年份
    def get_time_year(self):
        return datetime.datetime.now().year
    # 获取当前月份
    def get_time_month(self):
        return datetime.datetime.now().month
    # 获取当前日
    def get_time_day(self):
        return datetime.datetime.now().day
    # 获取当前时间日期（年月日）
    def get_time_date(self):
        return datetime.datetime.now().date()
    # 获取当前小时
    def get_time_hour(self):
        return datetime.datetime.now().time().hour
    # 获取当前时间
    def get_date_time (self):
            return datetime.datetime.now()

    # 获取当前周几
    def get_date_weekday(self):
        d = datetime.datetime.now().weekday()
        if d == 0:
            return '周一'
        elif d == 1:
            return '周二'
        elif d == 2:
            return '周三'
        elif d == 3:
            return '周四'
        elif d == 4:
            return '周五'
        elif d == 5:
            return '周六'
        elif d == 6:
            return '周日'
        else:
            raise RuntimeError('获取周几出错')

    # 获取当前年月日时分秒
    def get_ymdhm(self):
        return time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

