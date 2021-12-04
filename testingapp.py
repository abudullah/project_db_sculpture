from flask import Flask,render_template
import takinguserdata

app = Flask(__name__)

@app.route("/")
def hello_world():
    s="userprofile/24035b8a4d25aa6594457b4f894d3c55/Pytorch_logo.png"
    data=takinguserdata.userdata()
    

    return render_template("artist_dashboard.html",source=s,datum=data)
if __name__ == "__main__":
    app.run(debug=True,host='192.168.0.103', port=50)
    