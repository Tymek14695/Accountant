from app import app
from flask import render_template, request, redirect, url_for
import requests
import os
from bs4 import BeautifulSoup
import datetime

def report(action:object):
    with open('RoutesLog.log', 'a', encoding='utf-8') as log:
        log.write('\n<' + str(datetime.datetime.now()) + '>\t<' + __name__ + '>\t\n<' + action + '>\n')
    return action


@app.route('/')
@app.route('/index')
def index():
    report
    return report(render_template('index.html'))


