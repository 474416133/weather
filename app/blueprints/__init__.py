#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> __init__.py
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 16:46
@Desc   ：
"""

from . import  api
from . import page


def init_app(app):
    api.bp.register(app, {})
    page.bp.register(app, {})
