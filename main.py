""" In this module we are going to learn about working of sql commands through python using a connector
we will be using mysql workbench but we can connect to any of the database like oracle, mssql or mysql by installing their conector

we use to CRUD operation from here to
Create
Read
Update
Delete

The different steps involved in connecting to a database and do some basic operations are:
Install connector - we have to install a connector in our venv for connecting to different database we have different connector.
import the module into our programme. importing the connector to our programe
then create a connection for the database using the credentials, we can also create a config files and import it as a module in our program to hide the creadentials from users.
then using the connection we have to create a cursor object - This cursor object contains all the data that we get from a database.
So, if we are running a read command on our database then cursor will contain all the data, then we are going to fetch the data from cursor using fetchone() or 
fetchall() command.
fetchone() will fetch only a single record at a time while fetchall() will fetch all the records present in cursor.
using the cursor we can read and write on the database.
All the operations that we do on the database are executed through cursor.execute(str).
The str contains the command to run on database. we can do CRUD operation as stated above.
"""
