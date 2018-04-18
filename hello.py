from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Mu minimal ec2 example, v2!\n"

