import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
if conn.is_connected():
    print("connected")
