#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> __init__.py
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 19:45
@Desc   ：
"""
from flask import Blueprint

from . import v1


bp = Blueprint(name='weather', import_name=__name__, url_prefix='/weather')
bp.register_blueprint(v1.bp)

