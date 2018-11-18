import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='testdb')
cursor = conn.cursor ()
cursor.execute ("SELECT 100000000000000")
row = cursor.fetchone ()
print("MySQL server version:", row[0])
cursor.close ()
conn.close ()