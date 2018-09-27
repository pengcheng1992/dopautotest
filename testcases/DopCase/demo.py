from conf.EnvConf import sysconf as sc
from pagelib.baselib.Element import pucom
from testdata.BaseData import ld
try:
    print(pucom.get_data({
                sc.qa:{"username":"pengcheng2819","password":"pengcheng2819"} ,
                sc.yz: {"username":"pengcheng2819","password":"pengcheng2819"},
                sc.prod: {"username":"pengcheng2819","password":"pengcheng2819"}
            }))
except:
    print("获取字典出错")

