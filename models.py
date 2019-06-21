#!/usr/bin/env python
#coding:utf-8

from flask import Flask, redirect, url_for, render_template, session, g, jsonify, request
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)