from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quizdb'
app.config['MONGO_AUTH_SOURCE'] = 'admin'
app.config['MONGO_URI'] = 'mongodb://root:root@<url>:27017/admin'

mongo = PyMongo(app)
@app.route('/')
def admin():  
    return render_template('index.html')



def get_db():
    ## connection a la bdd mongo
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='root',
                         password='root',
                         authSource="admin")
    db = client["quizdb"]
    return db

@app.route('/listq', methods = ['GET'])
def get_animals():
    db = get_db()
    _questions = db.question.find({}) ## find toutes les questions
    return render_template('index.html', results = _questions)


@app.route('/mongo', methods=['GET'])
def get_all_docs():
    db = get_db()
    doc = db.question.insert_one({'abcd':'abcd'})   ## entre 1 document dans la bdd
    return "Inserted"
@app.route('/insert', methods=['GET'])
def insertData():
    db = get_db()
    url = request.form['question']
    answer = request.form['answer']
    dict = {"url":url,"answer":answer}
    db.question.insert_one({"url":url,"answer":answer})  ## récupère les informations depuis la formulaire et les entres dans la base
    return render_template('index.html', results = dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0')