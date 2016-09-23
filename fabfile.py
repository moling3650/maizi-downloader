#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-22 19:10:38
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : $Id$
import os
import requests
import io
import bs4
from fabric.api import *

BASE_DIR = os.getcwd()
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
URL = 'http://www.maiziedu.com/course/%d/'


@task(alias='dl')
def download(num):
    '''
    下载课程，要求一个参数num：课程编号
    '''
    # 抓取课程主页的内容写content.txt文件
    r = requests.get(URL % int(num))
    with io.open('content.txt', 'wb') as f:
        f.write(r.content)

    # 用BeautifulSoup提取课程的所有名字和连接
    soup = bs4.BeautifulSoup(io.open('content.txt', encoding='utf-8'), 'html.parser')

    lessons = {}
    for lesson in soup.select('.lesson-lists > li > a'):
        url = 'http://www.maiziedu.com' + lesson.get('href')
        lessons[lesson.find(class_='fl').text.encode('gbk')] = url

    if not os.path.exists(TEMP_DIR):
        local('mkdir ' + TEMP_DIR)

    with lcd(TEMP_DIR):
        for name, url in lessons.items():
            local('you-get -O temp.mp4 %s' % url)
            local('move temp.mp4 %s.mp4' % (''.join(name.split())))

    with lcd(BASE_DIR):
        local('ren temp ' + soup.title.text.encode('gbk'))

    if os.path.isfile('content.txt'):
        local('del content.txt')
