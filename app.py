import socket

from flask import Flask

app = Flask(__name__)
counter = 0


@app.get("/")
def greeting():
    return f"Hello from {socket.gethostname()}!"


@app.get("/counter")
def increment_counter():
    global counter
    counter += 1
    return str(counter)
