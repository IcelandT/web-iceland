# -*- coding: utf-8 -*-
# @Time    : 2022/7/7 22:34
# @Author  : IcelandPq
# @FileName: config.py


# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = 'tmc010928'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'pq020018andtmq010928'



JSON_AS_ASCII = False       # 设置ASCII编码格式

MAIL_SERVER = "smtp.qq.com"         # qq邮箱
MAIL_PORT = 465         # 端口
MAIL_USE_SSL = True         # qq邮箱使用的SSL协议
MAIL_USE_TSL = False
MAIL_DEBUG = True
MAIL_USERNAME = "1185330343@qq.com"
MAIL_PASSWORD = "twtvfmwbcmkibaad"
MAIL_DEFAULT_SENDER = "1185330343@qq.com"