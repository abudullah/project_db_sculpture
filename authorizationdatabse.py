import connection
cursor=connection.cursor()
sql="create table authorization (foldername varchar(150) not null,filename varchar(150) not null, authorized varchar(2))"
cursor.excute(sql)
connection.mydb.commit()

