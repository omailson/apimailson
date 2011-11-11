#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

from datetime import date
from glob import glob
import calendar
import xml.dom.minidom
import re

def render_calendar(dom, month=None, year=None):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    today = date.today()
    if month is None:
        month = today.month
    if year is None:
        year = today.year

    calendar.setfirstweekday(calendar.SUNDAY)
    calendario = calendar.monthcalendar(year, month)

    pattern = re.compile("w([1-6])d([1-7])")

    for nodes in dom.getElementsByTagName('text'):
        mat = pattern.match(nodes.attributes["id"].value)
        if nodes.attributes["id"].value == 'month':
            nodes.firstChild.firstChild.data = months[month - 1]
        elif nodes.attributes["id"].value == 'year':
            nodes.firstChild.firstChild.data = year
        elif mat != None:
            w = int(mat.group(1)) - 1
            d = int(mat.group(2)) - 1
            if w < len(calendario):
                if calendario[w][d] == 0:
                    nodes.firstChild.firstChild.data = ''
                else:
                    nodes.firstChild.firstChild.data = calendario[w][d]
            else:
                nodes.firstChild.firstChild.data = ''

    return dom

if __name__ == '__main__':
    today = date.today()

    year = raw_input('Year [%d]: ' % (today.year))
    if year.isdigit():
        year = int(year)
    else:
        year = None

    month = raw_input('Month [%d]: ' % (today.month))
    if month.isdigit():
        month = int(month)
    else:
        month = None

    filesList = glob('*.svg')
    if len(filesList) == 0:
        fileHandle = raw_input('Insert calendar template: ')
    else:
        i = 0
        print 'Choose calendar template: '
        for j in filesList:
            i = i + 1
            print i, j
        fileHandle = filesList[input('Choice: ') - 1]

    dom = render_calendar(xml.dom.minidom.parse(fileHandle), month, year)

    targetFile = raw_input('Insert target file name: ')
    targetHandle = open(targetFile, 'w')
    targetHandle.write(dom.toxml().encode('UTF-8'))
    targetHandle.close()
    print 'Done!'
