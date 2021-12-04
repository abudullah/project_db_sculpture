
import os 
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

print(currentdir,parentdir)

import connection
cursor=connection.cursor()
sql="create table sculpturedetail_table (filepath varchar(300),folder varchar(150),sculpturename varchar(40),price varchar(123),style varchar(120),creationdate varchar(120),uniqueidentity varchar(250))"

cursor.execute(sql)
connection.mydb.commit()


