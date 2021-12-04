import connection
con=connection.cursor()
def uniquepath(foldername,filepath,uniqueidentity):
  sql="INSERT INTO uniquepathidentityandpermission (foldername,filepath,uniqueidentity) VALUES (%s,%s,%s)"
  values=(foldername,filepath,uniqueidentity)
  con.execute(sql,values)
  connection.mydb.commit()

