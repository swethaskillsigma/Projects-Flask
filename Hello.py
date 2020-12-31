from flask import Flask

app=Flask(__name__)# creating the Flask class object

@app.route('/')#decorator 
def hello():
    return "Hello, welcome to Flask"

@app.route('/hello')#decorator 
def greet():
    return "Hello, welcome to Flask Routing"


if __name__=='__main__':
    app.run(debug=True)
