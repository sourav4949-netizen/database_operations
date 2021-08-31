import mysql.connector
def delete(id):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
    if conn.is_connected():
        print("connected to mysql db")
        cursor=conn.cursor()
        str="delete from emp where id ='%d'"
        args=id
        try:
            cursor.execute(str %args)
            conn.commit()
            print("employee deleted")
        except:
            conn.rollback
        finally:
            cursor.close()
            conn.close()

delete(2)
