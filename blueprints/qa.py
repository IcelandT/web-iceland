# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 14:42
# @Author  : IcelandPq
# @FileName: qa.py

from flask import Blueprint, render_template, g
from decorators import login_required


bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/docs')
# 判断是否登入，如果未登入这无法进入此页面
# @login_required
# 判断是否登入，如果未登入这无法进入此页面
def docs():
    return render_template('docs.html')


@bp.route('/MiHoYo')
def MiHoYo():
    '''
    原神板块
    :return:
    '''
    return render_template('MiHoYo.html')


@bp.route('/CSGO')
def CSGO():
    '''
    CSGO板块
    :return:
    '''
    return render_template('CSGO.html')


@bp.route('/ce')
def ce():
    '''
    CSGO板块
    :return:
    '''
    return render_template('测试.html')