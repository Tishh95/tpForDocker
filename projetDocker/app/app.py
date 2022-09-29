from flask import Flask
import mysql.connector
from typing import List, Dict
import json
from flask import render_template, request
app = Flask(__name__)
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'database': 'test'
    }

def submitPerson():
    return 'add'

def getPerson():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM persons')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return str(results)


@app.route('/',methods=['GET'])
def hello():
     results = json.dumps({'persons': getPerson()})
     return render_template('index.html', results = results)


@app.route('/form',methods=['POST'])
def form():
     return render_template('formperson.html')

@app.route('/salut')
def salutetlenom():
    return 'je suis quentin'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
