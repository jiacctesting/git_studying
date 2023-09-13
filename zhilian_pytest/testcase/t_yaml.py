import yaml

with open("../data/data.yaml","r",encoding="utf-8") as f:
    # r=yaml.safe_load(f)#读取单个文件
    # print(r)
    r=yaml.safe_load_all(f)
    for i in r:
        print(i)