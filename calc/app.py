import operations
from flask import Flask, request
app = Flask(__name__)



@app.get('/add')
def add():
    """add two numbers together"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    html = f"<html><body><h1>{operations.add(a,b)}</h1></body></html>"

    return html

@app.get('/sub')
def sub():
    """sub two numbers together"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    html = f"<html><body><h1>{operations.sub(a,b)}</h1></body></html>"

    return html

@app.get('/mult')
def mult():
    """mult two numbers together"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    html = f"<html><body><h1>{operations.mult(a,b)}</h1></body></html>"

    return html

@app.get('/div')
def div():
    """div two numbers together"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    html = f"<html><body><h1>{operations.div(a,b)}</h1></body></html>"

    return html