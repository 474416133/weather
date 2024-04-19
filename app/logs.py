#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> logs
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/16 16:47
@Desc   ：
"""

from logging import config
from . import logconfig


def init_app(app=None):
    """
    :param app:
    :return:
    """
    config.dictConfig(logconfig.DEFAULT_LOGGING)

