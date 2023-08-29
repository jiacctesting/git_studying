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

sql="select * from user_profile;"

cur.execute(sql)
#取一条数据
# one_row=cur.fetchone()

#取多条数据
# many_row=cur.fetchmany(5)#类似文件读取时的偏移量，之前取过一条数据，那这次就会从之前取的位置继续取，而不是从开头算

#取所有数据,无论取多少条，取出来的都是一个元组；根据取值的条数，一个元组内包含多个元组值
all_row=cur.fetchall()
print(all_row)
print(all_row[0][1])

# print(one_row)
# print(many_row)
cur.close()
db.close()