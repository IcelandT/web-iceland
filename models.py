# -*- coding: utf-8 -*-
# @Time    : 2022/7/14 20:53
# @Author  : IcelandPq
# @FileName: models.py

from exts import db
from datetime import datetime


class EmailCaptchaModel(db.Model):
    ''' 邮箱验证码模型 '''
    __tablename__ = 'email_captcha'     # 表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary_key设为主键, autoincrement自增长
    email = db.Column(db.String(100), nullable=False, unique=True)  # unique 只能存在一个  nullable 是否允许为空
    captcha = db.Column(db.String(5), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())  # 获取存储时当前的时间


class UserModel(db.Model):
    ''' 用户信息模型 '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now())


class MiHoYo(db.Model):
    ''' 原神用户模型 '''
    __tablename__ = 'MiHoYo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户uid
    uid = db.Column(db.String(30), nullable=False, unique=True)
    # 用户cookie
    cookie = db.Column(db.String(350), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now())
