import os 
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import connection
cursor=connection.cursor()
#sql="create table usertable (username varchar(150) not null,email varchar(250) not null,password varchar(40) not null,usercountry varchar(150) ,userprofile varchar(150) )"
sql="create table usertable (email varchar(250) not null,password varchar(40) not null,firstname varchar(250) not null,country varchar(250) not null,foldername varchar(150),filepath varchar(300) not null)"

cursor.execute(sql)
connection.mydb.commit()
