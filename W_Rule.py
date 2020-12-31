from flask import Flask
app=Flask(__name__)# creating the Flask class object

@app.route('/routing')#decorator 
def hello_route():
    return "hello, welcome to Flask for Routing"

@app.route('/wroute/')#decorator 
def hello_wroute():
    return "hello, WERKZUG's Routing"

if __name__=='__main__':
    app.run(debug=True)
