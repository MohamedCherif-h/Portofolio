from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/info")
def info ():
    return render_template ('info.html')

@app.route("/resume")
def resume ():
    return render_template ('resume.html')
