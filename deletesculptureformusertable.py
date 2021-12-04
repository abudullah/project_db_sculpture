import connection
def deletsculpture(identity):

    cur=connection.cursor()
    sql="delete from sculpturedetail_table  where uniqueidentity=%s"
    value=(identity,)
    cur.execute(sql,value)
    
