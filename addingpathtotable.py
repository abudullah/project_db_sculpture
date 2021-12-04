import connection
con=connection.cursor()
def insertvalues(folder,path,filename):
    sqlcmd="INSERT INTO path_table (foldername,path,filename) VALUES (%s,%s,%s)"
    values=(folder,path,filename)
    con.execute(sqlcmd,values)
    connection.mydb.commit()
    