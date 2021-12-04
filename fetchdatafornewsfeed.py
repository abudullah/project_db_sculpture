import connection
def fetchthedata():
 curr=connection.cursor()
 sql=("select sculpturename, sculpturedetail_table.filepath, firstname from sculpturedetail_table inner join usertable  on sculpturedetail_table.folder = usertable.foldername")
 curr.execute(sql)

 return curr.fetchall()