import os 
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print(parentdir)
sys.path.append(parentdir)

import connection
cursor=connection.cursor()
sql="create table admintable (emailaddress varchar(250) not null,password varchar(250))"
cursor.execute(sql)
connection.mydb.commit()
