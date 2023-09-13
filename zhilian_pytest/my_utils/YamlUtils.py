import os,yaml

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf=yamlf
        else:
            raise FileNotFoundError("文件地址不正确")
        self._data=None
        self._data_all=None

    def data(self):
        if not self._data:
            with open(self.yamlf,"r",encoding="utf-8") as f:
                self._data =yaml.safe_load(f)
        return self._data

    def data_all(self):
        if not self._data:
            with open(self.yamlf,"r",encoding="utf-8") as f:
                self._data_all=yaml.safe_load_all(f)
                #因为with循环外会关闭文件，无法读取生成器，所以将其转化成list
                self._data_all=list(self._data_all)
        return self._data_all


if __name__ == '__main__':
    r=YamlReader("../configs/conf.yaml").data()
    print(r)
    # r=YamlReader("../data/data.yaml").data_all()
    # for i in r:
    #     print(i)