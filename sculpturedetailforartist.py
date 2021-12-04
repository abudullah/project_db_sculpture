import connection
def sculpturedata(folder):

    cur=connection.cursor()
    sql="select  filepath,folder,sculpturename,price,style,creationdate,uniqueidentity from  sculpturedetail_table  where folder=%s"
    value=(folder,)
    cur.execute(sql,value)
    data=cur.fetchall()
    res = list(set(data))
    return res

