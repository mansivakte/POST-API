from flask import Blueprint, Flask, jsonify, request
from .model import Post
from app.db import db
import datetime

post_blueprint = Blueprint('post_blueprint', __name__)

#CREATE POST >>> POST REQUEST
@post_blueprint.route('/posts', methods= ['POST'])
def createPost():
    payload = request.json
    post = Post(title = payload['title'], body = payload['body'])
    db.session.add(post)
    db.session.commit()
    return {"status": "sucessfully done"}

#GET ALL POSTS >>> GET REQUEST
@post_blueprint.route('/posts', methods= ['GET'])
def getAllPost():
    try:
        post = Post.query.filter_by(is_deleted = False).all()
        newdict = []
        for i in post:
            a = {
                'id':i.id,
                'title':i.title,
                'body':i.body,
                'created_date':i.created_date,
                'published_date': i.published_date

            }
            newdict.append(a)
        return {'status': True, 'message':'', 'data':newdict }
    except Exception as e:
        print(e)
        return {'status': False, 'message':'something went wrong', 'data':None } 

#GET POST BY ID >>> GET REQUEST
@post_blueprint.route('/posts/<id>', methods= ['GET'])
def getPostbyId(id):
    try:
        post = Post.query.filter_by(id=id).first()
        a = {
            'id':post.id,
            'title':post.title,
            'body':post.body,
            'created_date':post.created_date,
            'published_date': post.published_date
        }
        return {'status': True, 'message':'', 'data':a}
    except:
        return {'status': False, 'message':'something went wrong', 'data':None}

#UPDATE POST >>> PUT REQUEST
@post_blueprint.route('/posts/<id>', methods= ['PUT'])
def update(id):
    try:
        payload = request.json
        post = Post.query.filter_by(id=id).first()
        post.title = payload['title']
        post.body = payload['body']
        db.session.commit()
        return {'status': True, 'message':'', 'data': '' }
    except:
        return {'status': False, 'message':'something went wrong', 'data':None }

#DELETE POST >>> DELETE REQUEST
@post_blueprint.route('/posts/<id>' , methods= ['DELETE'])
def delete(id):
    try:
        post = Post.query.filter_by(id=id).first()
        post.is_deleted = True
        db.session.commit()
        return {'status': True, 'message':'', 'data': '' }
    except: 
        return {'status': False, 'message':'something went wrong', 'data':None }

@post_blueprint.route('/posts/<id>', methods= ['PATCH'])
def published(id):
    try:
        post = Post.query.filter_by(id=id).first()
        post.published = True
        post.published_date = datetime.datetime.now()
        db.session.commit()

        return {'status': True, 'message':'', 'data':'' }
    except:
        return {'status': False, 'message':'something went wrong', 'data':None}
