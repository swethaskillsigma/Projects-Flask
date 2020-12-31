#datatype
from flask import Flask,render_template
app=Flask(__name__)# creating the Flask class object
@app.route('/score/<int:marks>')#decorator 

def message(marks):
    return render_template('delimiter2.html',mark=marks) 

if __name__=='__main__':
    app.run(debug=True)