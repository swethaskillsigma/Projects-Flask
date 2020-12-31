#multiparameter

from flask import *
app=Flask(__name__)# creating the Flask class object

@app.route('/result')#decorator 

def data():
    dict={'Physics':60,'Maths':80}
    return render_template('delimiter3.html',result=dict) 

if __name__=='__main__':
    app.run(debug=True)