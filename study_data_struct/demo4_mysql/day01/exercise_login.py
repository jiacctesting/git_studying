"""
用户选择注册或登录
"""
import pymysql

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="stu",
    charset="utf8"
)
cur=db.cursor()
def register():
    name=input("用户名：")
    password=input("密 码：")
    sql="select * from stu_new where user='%s'"%name
    print(sql)
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return False
    try:
        sql="insert into stu_new(user,password) values(%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True
    except Exception :
        db.rollback()
        return False

def login():
    name = input("用户名：")
    password = input("密 码：")
    sql = "select * from stu_new where user='%s' and password='%s'" % (name,password)
    print(sql)
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return True
    #可以不用谢result为假的情况，因为不执行上边的return True的话，函数会默认返回none
while True:
    print("""
    ========
    1:注册
    2:登录
    """)
    cmd=input("请选择：")
    if cmd=="1":
        result=register()
        if result:
            print("注册成功")
        else:
            print("注册失败")
    elif cmd=="2":
        result=login()
        if result:
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("无法完成选择的操作")


cur.close()
db.close()