import connection
con=connection.cursor()
def sculpturedata(filepath,folder,sculpturename,price,style,creationdate,uniqueidentity):
  sql="INSERT INTO sculpturedetail_table (filepath,folder,sculpturename,price,style,creationdate,uniqueidentity) VALUES (%s,%s,%s,%s,%s,%s,%s)"
  values=(filepath,folder,sculpturename,price,style,creationdate,uniqueidentity)
  con.execute(sql,values)
  connection.mydb.commit()