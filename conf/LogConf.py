# -*- coding:utf8 -*-
# create by pengcheng

import logging
class LogConf(object):
    html_type = ".html"
    log_par_path = "testlog/"
    log_level = logging.INFO
    logger_name = "html_logger"
    file_name = None
    mode = 'w'
    log_title = "测试用例"
    log_version = "DOP V3.23"
    shot_path = "screenshot/"
    shot_show_path = "/dopautotest/screenshot/"
    shot_type = ".png"
lc = LogConf()