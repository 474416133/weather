#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> encoder
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 17:47
@Desc   ：
"""
import json
import datetime
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.orm import class_mapper
from sqlalchemy.engine.result import RowProxy
from flask import current_app


def get_column_names(model_cls):
    """

    :param model_cls:
    :return:
    """
    return (c.name for c in class_mapper(model_cls).c)


class AlchemyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o.__class__, DeclarativeMeta):
            data = {}
            fields = o.__json__() if hasattr(o, '__json__') else get_column_names(o.__class__)
            for field in fields:
                value = o.__getattribute__(field)
                data[field] = self.default(value)
            return data
        elif isinstance(o, RowProxy):
            data = {}
            for field in o.keys():
                data[field] = self.default(o[field])
            return data
        elif isinstance(o, datetime.datetime):
            return o.strftime(current_app.datetime_format)
        elif isinstance(o, datetime.date):
            return o.strftime(current_app.date_format)
        elif isinstance(o, (list, dict, str, int, float, bool, type(None))):
            return o