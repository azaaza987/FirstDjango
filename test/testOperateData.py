import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "testdb")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
db.close()







conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db="testdb");
#创建游标
cursor = conn.cursor()
data = [
 ("N1",23,"2015-01-01","M"),
 ("N2",24,"2015-01-02","F"),
 ("N3",25,"2015-01-03","M"),
]
#执行sql，并返回受影响的行数
effect_row = cursor.executemany("insert into student (name,age,register_date,gender)values(%s,%s,%s,%s)",data)
conn.commit()