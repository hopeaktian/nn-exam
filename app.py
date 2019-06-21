#!/usr/bin/env python
#coding:utf-8

from flask import Flask

app = Flask(__name__)


# home_page
@app.route('/')
def index():
    return 'index page!'



if __name__ == '__main__':
    app.run()
