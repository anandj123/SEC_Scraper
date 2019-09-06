import mysql.connector

mydb = mysql.connector.connect(
    user='aman',
    password='pp',
    host='localhost',
    auth_plugin='mysql_native_password'
)
print(mydb)