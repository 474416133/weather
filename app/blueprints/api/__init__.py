#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> __init__.py
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 16:47
@Desc   ：
"""
from flask import Blueprint

from . import weather


bp = Blueprint(name='api', import_name=__name__, url_prefix='/api')
bp.register_blueprint(weather.bp)