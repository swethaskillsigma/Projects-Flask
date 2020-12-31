import os
import cx_Oracle # pip install cx_Oracle
from flask import Flask

db_user = os.environ.get('DBAAS_USER_NAME', 'hr')
db_password = os.environ.get('DBAAS_USER_PASSWORD', 'hr')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', 
"localhost:1521/xe")
service_port = port=os.environ.get('PORT', '8080')

app = Flask(__name__)

@app.route('/')
def index():
    connection = cx_Oracle.connect(db_user, db_password, db_connect)
    cur = connection.cursor()
    cur.execute("SELECT 'Hello, World from Oracle DB!' FROM DUAL")
    col = cur.fetchone()[0]
    cur.close()
    connection.close()
    return col

if __name__ == '__main__':
      app.run()
#host='localhost', port= int(service_port) )
