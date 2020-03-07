# coding: utf-8
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from App.ext import db


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Integer)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))
    head_portrait = db.Column(db.String(300))
    register_time = db.Column(db.DateTime)
    is_forbidden = db.Column(db.Boolean, default=False)


class Article(db.Model):
    __tablename__ = 'article'

    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aname = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(10000))
    create_time = db.Column(db.DateTime, default=datetime.now)
    # uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    cid = db.Column(db.Integer, db.ForeignKey('category.cid', ondelete='CASCADE'))
    hits = db.Column(db.Integer, default=0)
    comments = db.Column(db.Integer, default=0)
    picture = db.Column(db.String(300))



class Comments(db.Model):
    __tablename__ = 'comments'

    comid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(300))
    comment_time = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    # aid = db.Column(db.Integer, db.ForeignKey('article.aid'))


class Category(db.Model):
    __tablename__ = 'category'

    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(50), nullable=False)
    article_number = db.Column(db.Integer, default=0)


class Tag(db.Model):
    __tablename__ = 'tag'

    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tname = db.Column(db.String(50), nullable=False)
    aid = db.Column(db.Integer, db.ForeignKey('article.aid'))
