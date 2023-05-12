# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 17:41
# @Author  : IcelandPq
# @FileName: forms.py

''' 验证表单模块 '''

import wtforms
from wtforms.validators import length, email, EqualTo   # EqualTo  验证是否相等
from models import EmailCaptchaModel, UserModel


class LoginForm(wtforms.Form):
    ''' 登入表单 '''
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=12)])


class RegisterForm(wtforms.Form):
    ''' 注册表单 '''
    username = wtforms.StringField(validators=[length(min=2, max=20)])  # 验证长度
    email = wtforms.StringField(validators=[email()])     # 验证邮箱 email()为函数
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=12, message='密码长度必须在6到12位之间!')])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message='输入的两次密码长度不相等!')])

    def validate_captcha(self, field):
        ''' 验证验证码是否与数据库中相等 '''
        captcha = field.data    # 验证码
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        # 如果不存在该模型或者验证码不匹配则抛出异常
        if not captcha_model or captcha_model.captcha != captcha:
            raise wtforms.ValidationError('验证码错误!')

    def validate_email(self, field):
        ''' 验证邮箱是否注册过 '''
        email = field.data
        user_model = UserModel.query.filter_by(email=email).first()
        # 判断邮箱是否存在于数据库当中
        if user_model:
            raise wtforms.ValidationError('该邮箱已被注册!')

