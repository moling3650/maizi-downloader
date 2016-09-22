#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-22 19:10:38
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : $Id$
import os
import requests
from io import open
from bs4 import BeautifulSoup
from fabric.api import *

BASE_DIR = os.getcwd()
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
URL = 'http://www.maiziedu.com/course/641/'

# 抓取课程主页的内容写content.txt文件
r = requests.get(URL)
with open('content.txt', 'wb') as f:
    f.write(r.content)

# 用BeautifulSoup提取课程的所有连接
soup = BeautifulSoup(open('content.txt', encoding='utf-8'), 'html.parser')
lesson_lists = soup.select('.lesson-lists > li > a')

data = {}
for lesson in lesson_lists:
    url = 'http://www.maiziedu.com' + lesson.get('href')
    data[lesson.find(class_='fl').text.encode('gbk')] = url


def download():
    if not os.path.exists(TEMP_DIR):
        local('mkdir ' + TEMP_DIR)

    for name, url in data.items():
        with lcd(BASE_DIR):
            local('you-get %s' % url)
            file = filter(lambda f: f.endswith('mp4'), os.listdir(BASE_DIR)).pop()
            local('move %s %s' % (file, TEMP_DIR))

        with lcd(TEMP_DIR):
            local('move %s %s.mp4' % (file, ''.join(name.split())))

    with lcd(BASE_DIR):
        local('ren temp ' + soup.title.text.encode('gbk'))

    if os.path.isfile('content.txt'):
        local('del content.txt')
