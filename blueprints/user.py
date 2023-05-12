# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 22:21
# @Author  : IcelandPq
# @FileName: user.py

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
import string
import random
from datetime import datetime
from .forms import RegisterForm, LoginForm
import hashlib


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)  # 验证
        # 如果验证通过
        if form.validate():
            email = form.email.data
            password = form.password.data
            hash_password = hashlib.md5(bytes('PQ', encoding='utf-8'))
            hash_password.update(bytes(password, encoding='utf-8'))
            # 查询
            user = UserModel.query.filter_by(email=email).first()
            if user and user.password == hash_password.hexdigest():
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash('邮箱不存在或密码输入错误!')
                return redirect(url_for("user.login"))
        else:
            flash('密码长度必须在6到12位之间!')
            return redirect(url_for("user.login"))


@bp.route('/logout')
def logout():
    # 退出登入，清除所有session
    session.clear()
    return redirect(url_for('qa.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # render_template 重定向
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)  # request.form 存储前端的form表单
        # 如果验证通过
        if form.validate():
            # 获取表单信息
            username = form.username.data
            email = form.email.data
            password = form.password.data
            # 对密码进行加密
            hash_password = hashlib.md5(bytes('PQ', encoding='utf-8'))
            hash_password.update(bytes(password, encoding='utf-8'))
            user = UserModel(username=username, email=email, password=hash_password.hexdigest())
            db.session.add(user)
            db.session.commit()  # 提交表单
            return redirect(url_for('user.login'))  # 重定向, 将网页转到登入界面
        else:
            flash(form.errors['{}'.format(list(form.errors.keys())[0])][0])
            return redirect(url_for('user.register'))


@bp.route('/captcha', methods=['POST'])
def get_captcha():
    email = request.form.get('email')   # args GET请求 form 表单 POST请求
    # 随机拼接4位长度的验证码
    captcha = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    if email:
        message = Message(
            subject="注册验证码",
            recipients=['1185330343@qq.com'],
            body=f"【TengPQ】您的注册验证码为: {captcha} \n告诉别人是傻逼!"
        )
        mail.send(message)      # 发送邮件
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first() # 查询邮箱情况
        if captcha_model:
            # 如果邮箱已被注册，则更新数据库中验证码和发送时间
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            # 如果没被注册，则提交用户注册信息
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)   # 提交用户注册信息存入库
            db.session.commit()
        print('验证码:', captcha)
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 400, "message": "未传入邮箱!"})