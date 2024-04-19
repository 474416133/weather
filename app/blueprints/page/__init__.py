#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> __init__.py
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 16:47
@Desc   ：
"""

import logging
from flask import Blueprint, render_template, request
from app.common.errors import BizError
from app.common.response import create_response
from app.managers import weather_mgr


logger = logging.getLogger('web')
bp = Blueprint(name='page',
               import_name=__name__,
               url_prefix='/')


@bp.route('', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        city = '广州'
    else:
        city = request.form['city']
    try:
        data = create_response('请输入要查询的城市', 0, weather_mgr.get_city_weather(city))
        if city != data['data']['city']:
            data['err_msg'] = '查询不到【{}】的天气信息, 返回【{}】的天气信息'.format(city, data['data']['city'])
            data['err_code'] = 9999
    except BizError as e:
        data = create_response(e.error_remark, e.error_code)
    except:
        logger.exception('something wrong')
        data = create_response('server internal ERROR ', 500, {})

    return render_template('index.html', **data)

