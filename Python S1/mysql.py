# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:08:32 2019

@author: yogesh.sharma1
"""

from mysql.connector import connection

conn = connection.MySQLConnection(user="root",password="root",
                           host="127.0.0.1", database="testdb")

cursor = conn.cursor()

table = "create table user5(id int primary key,name varchar(20), dept varchar(20))"
#cursor.execute(table)

insert = "insert into user5 values(1,'joy','IT'),(2,'yogesh','HR'),(3,'joy','L&D'),(4,'mike','IT')"

cursor.execute(insert)
conn.commit()

select = "select * from user5"

cursor.execute(select)

for x in cursor:
    print(x)