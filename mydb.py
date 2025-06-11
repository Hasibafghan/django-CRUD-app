# Install Mysql on your computer
# https://dev.mysq1.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '',
)
#.prepare .a- cursor . object
cursorObject = dataBase.cursor()

#.Create.a.database
cursorObject.execute("CREATE DATABASE CRUD_db")

print("All-Done!")
# Note: The above code is for creating a MySQL database named 'CRUD_db'. 