import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
if conn.is_connected():
    print("connected to mysql db")
cursor=conn.cursor()

cursor.execute('select * from emp')

row = cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()

cursor.close()
conn.close()