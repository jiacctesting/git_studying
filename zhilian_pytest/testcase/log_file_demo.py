import logging

#1；设置logger名称
logger=logging.getLogger("log_file_demo")
#2：设置log级别,# 设置此logger的最低日志级别，以后添加的Handler级别若是低于这个设置，则以这个设置为最低限制
logger.setLevel(logging.DEBUG)
#3：创建handler
fh_stream=logging.StreamHandler()
fh_file=logging.FileHandler("./test.log")
#4：设置日志级别
fh_stream.setLevel(logging.INFO)
fh_file.setLevel(logging.CRITICAL)
#5：定义输出格式
formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
fh_stream.setFormatter(formatter)
#6：添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
#7：输出

logger.debug('This is a debug message!')
logger.info('This is a info message!')
logger.warning('This is a warning message!')
logger.error('This is a error message!')
logger.critical('This is a critical message!')
