# -*- coding:utf8 -*-
# create by pengcheng
from pagelib.baselib.HtmlLogger import log
import os.path
class OsPath(object):
    # 获取当前目录
    def get_crr_path(self):
        return os.getcwd()
    # 判断目录是否存在
    def path_exists(self,dir):
        return os.path.exists(dir)
    # 获取父目录
    def get_par_path(self):
        return os.path.pardir
    # 判断目录是否存在，不存在则创建目录
    def path_exists_create(self,path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception:
                log.error ("创建【"+path+"】目录失败")


op = OsPath()
