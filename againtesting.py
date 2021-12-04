from flask import Flask,render_template,request
from flask.templating import render_template_string
from sculpturedata import sculpturedata
import usefulhasing
import takinguserdata
import sculpturedata
import filesys
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("addsculpture.html")


@app.route("/add_sculpture", methods=['POST','GET'])
def add_sculpture():
    
    if request.method == 'POST':
        name=request.form['sculpture_name']
        price=request.form['price']
        art_style=request.form['art_style']
        creationdate=request.form['creation_date']
        path="F:\webproject\static"
        folder="posts"
        folderpath="posts"
        kala=usefulhasing.u_and_p_hash("konterebin@gmail.com","meytera")#username or folder name
        if not filesys.folder_exist(path,folder):
              filesys.create_folder_for_user(path,folder)
            
        path=os.path.join(path,folder)
        
        if not filesys.folder_exist(path,kala):
                filesys.create_folder_for_user(path,kala)
                path=os.path.join(path,kala)
                folderpath="/".join([folderpath, kala])#this will go on path
        folderpath="/".join([folderpath, kala])
        path=os.path.join(path,kala)
               
        for upload in request.files.getlist("file"):
            print("mey tera",upload.filename)
            filename = upload.filename    #this will go on file name 
            print("sudir vai sudi ",filename)
                #   print(filename)
                #   destination=os.path.join(path,filename)
                #   # This is to verify files are supported
                #   upload.save(destination)
                #   return render_template("newsfeed.html")
            ext = os.path.splitext(filename)[1]
            if (ext == ".jpg") or (ext == ".png"):
                        print("File supported moving on...")
            
            
            destination = "/".join([path, filename])
            filepath="/".join([folderpath, filename])#this is the ultimate folder path
            kalabala=os.path.join(kala,filename)
            print("Accept incoming file:", filename)
            print("Save it to:", destination)
            sculpturedata.sculpturedata(filepath,kala,name,price,art_style,creationdate)
            upload.save(destination)
        
        
        
    return render_template("addsculpture.html")

if __name__ == "__main__":
    app.run(debug=True,host='192.168.0.103', port=55)