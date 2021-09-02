from Config_module import mysqlConfig
import mysql.connector

conn = mysql.connector.connect(**mysqlConfig)

if conn.is_connected():
    print("Connected to db")

    cursor = conn.cursor()
    cursor.execute('select * from emp')

onerow=cursor.fetchone()
while onerow:
    print(onerow)
    onerow = cursor.fetchone()

cursor.close()
conn.close()

