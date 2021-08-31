import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
if conn.is_connected():
    print("connected to mysql db")
cursor=conn.cursor()

try:
    cursor.execute("INSERT INTO emp values(7,'moti',55000)")
    conn.commit()
    print("employee added")
except:
    conn.rollback

cursor.close()
conn.close()