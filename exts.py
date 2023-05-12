# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 18:53
# @Author  : IcelandPq
# @FileName: exts.py

'''
实例化各类工具
数据库, 注册邮件发送
SQLAlchemy  Flask操作数据库的第三方插件
'''

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()