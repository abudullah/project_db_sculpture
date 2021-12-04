import os 
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print(parentdir)
sys.path.append(parentdir)

import connection
cursor=connection.cursor()
sql="create table uniquepathidentityandpermission (foldername varchar(150) not null,filepath varchar(300) not null,uniqueidentity varchar(300),permission varchar(10) DEFAULT 'NO')"
cursor.execute(sql)
connection.mydb.commit()

