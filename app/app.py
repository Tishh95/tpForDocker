from flask import Flask, jsonify, render_template, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='root',
                         password='root',
                        authSource="admin")
    db = client["quizdb"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

@app.route('/index', methods = ['GET'])
def get_animals():
    db = get_db()
    _questions = db.question.find({})
    return render_template('index.html',results = _questions)

@app.route('/admin', methods = ['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route('/database', methods = ['POST'])
def database():
    db = get_db()
    url = request.form['question']
    answer = request.form['answer']
    dict = {"url":url,"answer":answer}
    db.question.insert_one({"url":url,"answer":answer})
    return render_template('index.html', results = dict)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
