import datetime
import logging,os,sys
from configs.conf import MyConfigYaml,get_log_path

#定义日志级别的映射
log_l={
    "debug":logging.DEBUG,
    "info":logging.INFO,
    "error":logging.ERROR,
    "waring":logging.WARNING,
    "crtical":logging.CRITICAL,
}
class MyLogger:
    def __init__(self,log_file,log_name,log_level):
        self.log_file=log_file #文件格式的日志存储地址
        self.log_name=log_name
        self.log_level=log_level#从yaml文件读取

        # 1；设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 2：设置log级别,# 设置此logger的最低日志级别，以后添加的Handler级别若是低于这个设置，则以这个设置为最低限制
        self.logger.setLevel(log_l[self.log_level])
        # 3：创建handler
        fh_stream = logging.StreamHandler()
        fh_stream.setLevel(log_l[self.log_level])

        #判断handler是否存在，不存在再去创建：
        if not self.logger.handlers:
            formatter = logging.Formatter('%(asctime)s 模块位置：%(name)s  等级信息：%(levelname)s  信息详情：%(message)s ')
            # formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
            fh_stream.setFormatter(formatter)

            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            # 6：添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)

#初始化log_file,log_name,log_level
log_path=get_log_path()
current_time=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
log_extencison=".log"
logfile=os.path.join(log_path,current_time+log_extencison)  #文件式log的存储地址
# print(logfile)

loglevel=MyConfigYaml().get_conf_loglevel()

#log_name=os.path.basename(sys.argv[0])可以自动带上文件模块，也可以自己调用时设置参数
def my_log(log_name=os.path.basename(sys.argv[0])):
    return MyLogger(log_file=logfile, log_name=log_name, log_level=loglevel).logger

if __name__ == '__main__':
    my_log().info("info message")
    print(os.path.split(__file__)[1])
    print(os.path.basename(sys.argv[0]))