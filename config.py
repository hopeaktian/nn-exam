#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/12/1 12:09
author:    peak
description:
"""
class Config(object):
    SECRET_KEY = '7a71ea10c4sf9f16f3220488e215s32fd'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://nn-exam:nnexam520@localhost/nn-exam"
