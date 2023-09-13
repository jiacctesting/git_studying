import yaml,os
from my_utils.YamlUtils import YamlReader



#获取当前文件地址
current=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(current))
#BASE_DIR等价于os.path.dirname(os.path.dirname(__file__))
#config文件目录
_config_path=BASE_DIR+os.sep+"configs"
#yaml配置文件目录
_config_file=_config_path+os.sep+"conf.yaml"

#定义生成log文件的路径
_log_path=BASE_DIR+os.sep+"logs"

#获取配置文件目录地址
def get_config_path():
    return _config_path

#获取配置文件地址
def get_config_file():
    return _config_file

#获取log文件地址
def get_log_path():
    return _log_path

class MyConfigYaml:

    def __init__(self):
        self.config=YamlReader(get_config_file()).data()

    def get_conf_url(self):
        return self.config["Base"]["test"]["url"]

    def get_conf_loglevel(self):
        return self.config["Base"]["loglevel"]

if __name__ == '__main__':
    m=MyConfigYaml().get_conf_loglevel()
    print(m)