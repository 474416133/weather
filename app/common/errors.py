#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：lb_web -> error
@IDE    ：PyCharm
@Author ：sven
@Date   ：2022/2/9 14:55
@Desc   ：
"""

from enum import Enum


class BizError(RuntimeError):
    """
    业务异常
    """
    __slots__ = "error_code", "error_value", "error_remark"

    def __init__(self, error_code, error_value, error_remark=None, *args):
        self.error_code = error_code
        self.error_value, self.error_remark = error_value, error_value
        if error_remark:
            self.error_remark = error_remark
            if args:
                self.error_remark = self.error_remark.format(*args)

    def __str__(self):
        """
        @overide
        :return:
        """
        return f"error_code={self.error_code}," \
               f" error_value={self.error_value}," \
               f" error_remark={self.error_remark}"

    def as_dict(self):
        """

        :return:
        """
        return {
            "error_code" : self.error_code,
            "error_value" :self.error_value,
            "error_remark" : self.error_remark
        }


class IError(Enum):
    """
    异常
    """
    def exception(self, error_remark=None, *args):
        """
        异常
        :param msg:
        :param args:
        :return: BizError对象
        """
        return BizError(self.value, self.name, error_remark, *args)

    def reraise(self, error_remark=None, *args):
        """
        抛出异常
        :param remark:
        :param args:
        :return:
        """
        raise self.exception(error_remark, *args)