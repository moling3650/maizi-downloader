#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-24 17:47:28
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : $Id$
import sys
import you_get
import requests
from bs4 import BeautifulSoup

URL = 'http://www.maiziedu.com/course/%d/'
COMMAND = 'you-get -o {dir} -O {name}.mp4 {url}'


def download_by_index(number):
    response = requests.get(URL % number)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('.vlesson-infoR > h1').text.replace(' ', '').replace('-', '_')

    for lesson in soup.select('.lesson-lists > li > a'):
        url = 'http://www.maiziedu.com' + lesson.get('href')
        name = lesson.find(class_='fl').text.replace(' ', '').replace('-', '_')
        sys.argv = COMMAND.format(dir=title, name=name, url=url).split()
        you_get.main()


if __name__ == '__main__':
    for idx_or_range in sys.argv[1:]:
        if '~' in idx_or_range:
            start, end = map(int, idx_or_range.split('~'))
            for idx in range(start, end + 1):
                download_by_index(idx)
        else:
            download_by_index(int(idx_or_range))
