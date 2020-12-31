from flask import Flask

app=Flask(__name__)# creating the Flask class object

def greet():
    return "Hello, welcome to Flask Routing"
app.add_url_rule("/","hello",greet)

if __name__=='__main__':
    app.run(debug=True)
