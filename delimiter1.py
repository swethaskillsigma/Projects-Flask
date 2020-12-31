from flask import *
app=Flask(__name__)# creating the Flask class object
@app.route('/user/<uname>')#decorator 
def message(uname):
    return render_template('delimiter1.html',name=uname) 

if __name__=='__main__':
    app.run(debug=True)