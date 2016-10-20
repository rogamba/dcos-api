#-*- coding:utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import app.errors
import sys
import json
import app.db

# Iniciamos la base de datos
app.db.init()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.model import Post

# Home
@app.route('/')
@cross_origin(origin="*")
def main():
    return jsonify({
        'app' : 'DC/OS training app',
        'author' : 'Rodrigo Gamba',
        'date' : datetime.now()
    })

# HTTP Error handling
@app.errorhandler(404)
@cross_origin(origin="*")
def not_found(error):
    return jsonify({
        "error": "not found"
    }), 400

# HTTP Error handling
@app.errorhandler(400)
@cross_origin(origin="*")
def bad_request(error):
    return jsonify({
        "error": "bad request"
    }), 400

# Save item controller
@app.route('/save',methods=['POST','OPTIONS'])
@cross_origin(origin="*")
def save():
    params = request.get_json()
    # Salvamos el nuevo post
    try:
        Post.create(
            user=params['user'],
            text=params['text'],
            date=str(datetime.now())
        )
        result = True
        msg = "Record saved"
    except Exception as e:
        print(sys.exc_info())
        raise errors.ApiError("invalid_parameters", str(e))

    return jsonify({
        'result' : result,
        'msg' : msg
    })


# Save item controller
@app.route('/fetch',methods=['GET','OPTIONS'])
@cross_origin(origin="*")
def fetch():
    last_date = request.args.get('q')
    posts = Post.query.filter(Post.date > last_date).order_by(Post.date.desc()).all()
    if posts is not None:
        items = [ {'user' : row.user, 'text' : row.text, 'date' : row.date.strftime('%Y-%m-%d %H:%M:%S')} for row in posts ]
    else:
        items = []
    # Salvamos el nuevo post
    return jsonify({
        'items' : items
    })
