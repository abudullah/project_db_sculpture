from flask import Flask, redirect, url_for, render_template, request,logging,session,render_template_string
import filesys
import os
from sculpturedata import sculpturedata
import usersession,usefulhasing

import detectuser
import takinguserdata
import sculpturedetailforartist

import checkvalidtion,registeruser,deletesculptureformusertable
from flask.templating import render_template_string
import fetchdatafornewsfeed
import insertdataintouniquepathidentity
app = Flask(__name__,template_folder='templates')

app.secret_key='asdsdfsdfs13df_df%&'


@app.route("/")  # this sets the route to this page
def home():
        if 'userid' in session:
         
         
         return redirect("/newsfeed")
        else:
            return render_template("login.html")
@app.route("/adminpanel")
def adminpanel():
    return render_template("adminpanel.html")

@app.route("/adminloginpage")
def adminloginpage():
    return render_template("adminlogin.html")
@app.route("/adminlogin",methods=["POST"])

def adminlogin():
    
    if request.method == "POST":
        email=request.form['em']
        pw=request.form['pw']
        print(email,pw)
        if detectuser.adminlogin(email,pw):
         session['admin']="true"
         session['userid']=email
         session['pw']=pw
         print("i am here ")
         return redirect(url_for('adminpanel'))
    return render_template("adminlogin.html")
@app.route("/artistdashboard")
def artistdashboard():
    user=session['userid']
    pw=session['pw']
    print("my user",user)
    print("user password",pw)
    uperbar="USERHOME"

    if (detectuser.isadmin(user,pw)):
        uperbar="ADMIN_HOME"
    user=usefulhasing.u_and_p_hash(user,pw)
    print("why my hash",user)
    uerdata=takinguserdata.userdata(user)
    usersculpturedata=sculpturedetailforartist.sculpturedata(user) 

    return render_template("artist_dashboard.html",user=uperbar,userdetail=uerdata[0],datum=usersculpturedata)
@app.route("/deleteformuser/<q>")
def deleteformuser(q):
    deletesculptureformusertable.deletsculpture(q)
    

    return redirect (url_for('artistdashboard'))
    
   
@app.route("/editfromuser/<d>")
def editformuser(d):

    return redirect("artistdashboard")

@app.route("/loadsculpture")
def loadsculpture():
    return render_template("addsculpture.html")
@app.route("/add_sculpture", methods=['POST'])
def add_sculpture():
    if request.method == 'POST':
        sculpturename=request.form["sculpture_name"]
        price=request.form["price"]
        artstyle=request.form["art_style"]
        creationdate=request.form["creation_date"]
        email=session["userid"]
        pw=session["pw"]
        kala=usefulhasing.u_and_p_hash(email,pw) #this will go on folder
        path="F:\webproject\static"
        
        folderpath="posts"
        path=os.path.join(path,folderpath)
        folderpath="/".join([folderpath, kala])
        path2=os.path.join(path,kala)
  
        if not filesys.folder_exist(path):
            filesys.create_folder_for_user(path)
            
        
        if not filesys.folder_exist(path2):
                filesys.create_folder_for_user(path2)
               

        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            
            filename = upload.filename    #this will go on file name   
            destination = "/".join([path2, filename])
            filepath="/".join([folderpath, filename])
            
            
            
            filepathidentity=usefulhasing.p_hash(filepath)
            
            
            sculpturedata(filepath,kala,sculpturename,price,artstyle,creationdate,filepathidentity)
            insertdataintouniquepathidentity.uniquepath(kala,filepath,filepathidentity)

            upload.save(destination)
            return redirect(url_for('loadsculpture'))



   

@app.route("/newsfeed")
def newsfeed():
    user=session['userid']
    pw=session['pw']
    uperbar="USER_HOME"

    if (detectuser.isadmin(user,pw)):
        uperbar="ADMIN_HOME"
    
    
    result=fetchdatafornewsfeed.fetchthedata()
    print(result)
    return render_template("newsfeed.html",posts=result,user=uperbar)

@app.route("/buy/<q>")
def buy(q):
    print("fuck you ",q)
    return render_template_string("fuck you ")
    
@app.route("/login",methods = ['POST']) 
def login():
    if request.method == 'POST':
        print("i am here")

        if 'userid' in session:
            print("i am also here")
            return render_template("newsfeed.html")
        if request.method=="POST":
            user = request.form["em"]
            pw=request.form["pw"]
            print(user)
            print(pw)
            
            password =usefulhasing.p_hash(pw)
            if(checkvalidtion.em_exit(user,password)):

                session['userid']=user
                session['pw']=pw
                return redirect("/newsfeed")

            else:
                return render_template("login.html")
@app.route("/logout",methods=['GET'])

def logout():
    if request.method=="GET":
     if 'userid' in session:
          session.pop('userid',None)
          session.pop('pw',None)

     return render_template("login.html")
             
@app.route("/register")
def register():
    if 'userid' in session:
        return redirect("newsfeed")
    return render_template("sign_up.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
            if request.method == 'POST':
                email=request.form["email"]
                pw=request.form['pswd']
                firstname=request.form['firstname']
                country=request.form['country']
                if not checkvalidtion.isregisteredemail(email):
                        
                
                        registeruser.registration(email,pw)
                            
                        kala=usefulhasing.u_and_p_hash(email,pw) #this will go on folder
                        path="F:\webproject\static"
                        folder="userprofile"
                        folderpath="userprofile"
                        path=os.path.join(path,folder)
                        path2=os.path.join(path,kala)
                        folderpath="/".join([folderpath, kala])#this will go on path
                        
                        
                        print(kala)
                        
                        if not filesys.folder_exist(path):
                            filesys.create_folder_for_user(path)
                            
                            
                        if not filesys.folder_exist(path2):
                                filesys.create_folder_for_user(path2)
                       
                        for upload in request.files.getlist("file"):
                            print("mey tera",upload.filename)
                            filename = upload.filename    #this will go on file name 
                            print("sudir vai sudi ",filename)
                               
                            ext = os.path.splitext(filename)[1]
                            if (ext == ".jpg") or (ext == ".png"):
                                        print("File supported moving on...")
                            
                            
                            destination = "/".join([path2, filename])
                            filepath="/".join([folderpath, filename])#this is the ultimate folder path
                            
                            print("Accept incoming file:", filename)
                            print("Save it to:", destination)
                            
                            registeruser.start_with_hash_password(email,pw,firstname,country,kala,filepath)#registration done here
                            
                            
                            

                            session['userid']=email
                            session['pw']=pw
                            upload.save(destination)
                session['userid']=email
                session['pw']=pw
       
                return  redirect("newsfeed")
           
      
if __name__ == "__main__":
    app.run(debug=True,host='192.168.0.103', port=5000)
    