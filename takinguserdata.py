import connection
def userdata(folder):

    cur=connection.cursor()
    sql="select firstname,country,filepath from usertable where foldername=%s"
    value=(folder,)
    cur.execute(sql,value)
    data=cur.fetchall()
    return data

 
