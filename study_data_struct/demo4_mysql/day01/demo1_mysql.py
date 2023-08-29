import pymysql

db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   password="123456",
                   database="stu",
                   charset="utf8"
                   )
cur=db.cursor()
# cur.execute("create table stu_info(id int primary key)")
cur.execute("insert into stu_info values (1)")
db.commit()#写操作必须要使用commit提交才可以让数据库发生改变
# cur.execute("show tables")
cur.close()
db.close()