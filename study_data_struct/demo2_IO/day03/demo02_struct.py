"""
 将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据，进行解
析。

"""

from struct import *

#生成结构化对象
st=Struct("i4sf")

#将一组数据按照指定格式打包转换为bytes，注意s代表的是二进制的字节串，输出结果为字节串
data=st.pack(1,b"zhang",1.80)
print(data)

# 将bytes字节串按照指定的格式解析
un_data=st.unpack(data)
print(un_data)


st=pack("i2sf",1,b"zhang",1.80)
print(st)