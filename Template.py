from flask import Flask,redirect,url_for
app=Flask(__name__)# creating the Flask class object

@app.route('/hello')#decorator 
def hello_admin():
    return "<html><body><h1> Welcome to Flask Templates</h1></body></html>"

if __name__=='__main__':
    app.run(debug=True)