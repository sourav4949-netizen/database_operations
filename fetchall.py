import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
if conn.is_connected():
    print("connected to mysql db")
cursor=conn.cursor()

cursor.execute('select * from emp')

rows = cursor.fetchall()
print("Total number off records is:", cursor.rowcount)
for row in rows:
    print(row)

cursor.close()
conn.close()