from flask  import Flask, redirect, url_for, render_template, request,logging
import checkvalidtion

app = Flask(__name__,template_folder='templates')
@app.route("/")  # this sets the route to this page
def home():
    return render_template("run.html")
if __name__ == "__main__":
    app.run(host='localhost', port=500)