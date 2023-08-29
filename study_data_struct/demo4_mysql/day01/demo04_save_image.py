import pymysql

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="niuke",
    charset="utf8"
)

cur=db.cursor()
#在数据库存储图片（二进制形式）
# with open ("test.PNG","rb") as f:
#     data=f.read()
#
# sql="update user_profile set image=%s where id=1;"
#
# cur.execute(sql,[data])
# db.commit()

#从数据库读图片
cur.execute("select image from user_profile where id =1;")
data=cur.fetchone()
with open ("save.png","wb") as f:
    f.write(data[0]) #需要注意取出来的是元组


cur.close()
db.close()