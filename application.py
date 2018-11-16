import os
import requests

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

lst = []
votes = {"yes":0, "no":0, "maybe":0}


@app.route("/")
def index():
    return render_template("index.html", votes=votes)

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("vote totals", votes, broadcast=True)

if __name__ == '__main__':
    #app.debug = True
    #app.run(host = '0.0.0.0',port=8900)
    socketio.run(app, host='0.0.0.0', port=8900)
