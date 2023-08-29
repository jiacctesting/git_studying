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

try:
    #写入数据
    id=input("id")
    evice_id=input("evice_id")
    gender=input("gender")
    university=input("university")
    #方法一
    sql='insert into user_profile (id,evice_id,gender,university) values \
        (%s,%s,"%s","%s")' %(id,evice_id,gender,university)
    #注意如果表里边的字段要求是字符串类型时，那在sql中的values中必须对字段加上双引号
    print(sql)
    cur.execute(sql)

    #方法2，通过列表给values后边传值
    sql = 'insert into user_profile (id,evice_id,gender,university) values \
            (%s,%s,%s,%s)'
    cur.execute(sql,[id,evice_id,gender,university])#一般只应用在insert语句中，并且只能给values传值，sql中全写成%s就可以，传的值就是input的那些
    db.commit()#写操作必须有commit才生效


except Exception as e:
    db.rollback()
    print(e)