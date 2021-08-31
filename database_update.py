import mysql.connector
def update(id):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Test12345')
    if conn.is_connected():
        print("connected to mysql db")
        cursor=conn.cursor()
        str="update emp set sal= 12225 where id ='%d'"
        # sal=(12225)
        args=(id)
        try:
            print("Inside try block")
            cursor.execute(str %args)
            conn.commit()
            print("employee updated")
        except:
            conn.rollback
            print("inside except block")
        finally:
            cursor.close()
            conn.close()

update(3)
