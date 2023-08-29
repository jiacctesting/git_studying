import yaml

#
# def get_yaml_data(fileDir):
#     # 1. 打开yaml文件
#     fo = open(fileDir,'r',encoding='utf-8')
#     # 2. 使用第三方库去获取
#     res = yaml.load(fo,Loader=yaml.FullLoader) # 处理警告
#     print(res)
#     print(res['info1'])
#     print(res['info2'])

def get_yamls_data(fileDir):
    '''
    des: 一个yaml文件内包含多个yaml数据
    :param fileDir:
    :return:
    '''
    # 1. 打开yaml文件
    fo = open(fileDir, 'r', encoding='utf-8')
    # 2. 使用第三方库去获取
    res = yaml.load_all(fo, Loader=yaml.FullLoader)  # 处理警告
    for one in res:
        print(one)


if __name__ == '__main__':
    get_yamls_data(r'C:\Users\Lenovo\PycharmProjects\study_data_struct\yaml_data.py')
    print("===========")
    # get_yaml_data(r'C:\Users\Lenovo\PycharmProjects\study_data_struct\yaml_data.py')
