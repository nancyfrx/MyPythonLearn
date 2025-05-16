#操作系统接口
import os
print(os.getcwd())
os.system("ls -ll")
print(dir(os))
#print(help(os))


#文件通配符
import glob
print(glob.glob('*.py'))


# 命令行参数
import sys
print(sys.argv)

# 字符串匹配
import  re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.split(',','112,214,124'))


# 时间类
from datetime import date
print(date.today())
print(date.today().strftime('%m-%d-%y'))

# 日志类
import  logging
logging.debug("debug---")
logging.error("error---")
logging.warning("warning---")
logging.info("info---")



