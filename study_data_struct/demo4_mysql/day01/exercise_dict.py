import pymysql

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="dictnary"
)

cur=db.cursor()



with open(r"C:\Users\Lenovo\Desktop\dict.txt","r",encoding="utf-8") as f:
    # content=f.readlines()
    # for item in content:
    #
    # print(description)
    while True:
        content=f.readline()
        if content =="":
            break
        tmp = content.split()
        word=tmp[0]
        description=" ".join(tmp[1:]).split()
        description_str=" ".join(description)
        try:
            sql="insert into dict(word,description) values(%s,%s)"
            cur.execute(sql,[word,description_str])
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

cur.close()
db.close()
