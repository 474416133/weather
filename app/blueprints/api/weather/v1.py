#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> v1
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 19:45
@Desc   ：
"""

from flask import Blueprint
from app.common.response import OK
from app.managers import weather_mgr

bp = Blueprint(name='weather::v1', import_name=__name__, url_prefix='/v1')


@bp.route('/city/<city>')
def get_city_weather(city):
    return OK(weather_mgr.get_city_weather(city))