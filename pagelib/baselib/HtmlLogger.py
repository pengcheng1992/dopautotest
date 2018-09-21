# -*- coding:utf8 -*-
# create by pengcheng
import logging
import os.path
import datetime
from conf.LogConf import lc
from pagelib.baselib.OsPath import op

#: HTML header (starts the document
_START_OF_DOC_FMT = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>%(title)s</title>
<style type="text/css">
body, html {
background: #000000;
font-family: Arial;
font-size: 16px;
color: #C0C0C0;
}
h1 {
color : #FFFFFF;
border-bottom : 1px dotted #888888;
}
pre {
font-family : arial;
margin : 0;
}
.box {
border : 1px dotted #818286;
padding : 5px;
margin: 5px;
background-color : #292929;
display:inline-block;
*display:inline;
*zoom:1;
}
.err {
color: #EE1100;
font-weight: bold
}
.warn {
color: #FFCC00;
font-weight: bold
}
.info {
color: #C0C0C0;
}
.debug {
color: #CCA0A0;
}
img{
max-width:800px;
}

</style>
</head>
<body>
<h1>%(title)s</h1>
<h3>%(version)s</h3>
<div class="box">
<table>
"""

_END_OF_DOC_FMT = """</table>
</div>
</body>
</html>
"""

_MSG_FMT = """
<tr>
<td class="%(class)s" ><pre>%(msg)s</pre></td>
<tr>
"""

_PIC_FMT = """
<tr>
<td class="%(class)s" ><a href="%(picsrc)s" target=“_blank“>
<img src="%(picsrc)s" alt="%(alt)s"/></a></td>
<tr>
"""

class HTMLFileHandler(logging.FileHandler):
    """
    File handler specialised to write the start of doc as html and to close it
    properly.
    """

    def __init__(self, title, version, *args):
        super().__init__(*args)
        assert self.stream is not None
        # Write header
        self.stream.write(_START_OF_DOC_FMT % {"title": title,
                                               "version": version})

    def close(self):
        # finish document
        self.stream.write(_END_OF_DOC_FMT)
        super().close()


class HTMLFormatter(logging.Formatter):
    """
    Formats each record in html
    """
    CSS_CLASSES = {'WARNING': 'warn',
                   'INFO': 'info',
                   'DEBUG': 'debug',
                   'CRITICAL': 'err',
                   'ERROR': 'err'}

    def __init__(self):
        super().__init__("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


    def format(self, record):
        try:
            class_name = self.CSS_CLASSES[record.levelname]
        except KeyError:
            class_name = "info"

        # handle '<' and '>' (typically when logging %r)
        msg = record.msg
        msg = msg.replace("<", "&#60")
        msg = msg.replace(">", "&#62")
        record.message = record.msg
        if msg.startswith("picshot_1") :
            msg = msg.replace("picshot_1","")
            return _PIC_FMT % {"class": class_name,"picsrc": msg,"alt":"用例失败截图"}
        else:
            if self.usesTime():
                record.asctime = self.formatTime(record, self.datefmt)
            s = self.formatMessage(record)
            if record.exc_info:
                # Cache the traceback text to avoid converting it multiple times
                # (it's constant anyway)
                if not record.exc_text:
                    record.exc_text = self.formatException(record.exc_info)
            if record.exc_text:
                if s[-1:] != "\n":
                    s = s + "\n"
                s = s + record.exc_text
            if record.stack_info:
                if s[-1:] != "\n":
                    s = s + "\n"
                s = s + self.formatStack(record.stack_info)

            return _MSG_FMT % {"class": class_name,"msg": s}


class HTMLLogger(logging.Logger):
    """
    Log records to html using a custom HTML formatter and a specialised
    file stream handler.
    """

    def __init__(self, name=lc.logger_name,level=logging.DEBUG,filename= None, mode='w',title=lc.log_title, version=lc.log_version):

        super().__init__(name, level)
        # 如果创建实例没有传路径，则使用项目下的testlog路径
        if filename == None:
            if lc.html_type.startswith("."):
                # 获取当前时间并且替换掉非法字符用来作为文件名
                rq = str(datetime.datetime.now()).replace(" ", "").replace(":", "").replace(".", "")
                # # 获取当前工程目录
                pwd = op.get_project_path()
                # 拼凑日志目录
                log_path =  pwd+"/"+lc.log_par_path + str(datetime.datetime.now().date()) + "/"
                # 判断目录是否存在，不存在则创建目录
                if not os.path.exists(log_path):
                    try:
                        os.makedirs(log_path)
                    except Exception:
                        raise ("创建日志目录失败")
                filename = log_path  + rq + lc.html_type
            else:
                raise ("文件类型请以.开始")
            # 创建formatter：日志输出格式
        f = HTMLFormatter()
            # 创建日志文件
        h = HTMLFileHandler(title, version, filename, mode,'utf-8')
            # 设置输出格式
        h.setFormatter(f)
        self.addHandler(h)





