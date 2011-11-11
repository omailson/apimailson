#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import calendar
import xml.dom.minidom
import re
import datetime
import glob

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

yearToday = datetime.date.today().year
monthToday = datetime.date.today().month
year = raw_input('Year [%d]:' % (yearToday))
if year.isdigit():
    year = int(year)
else:
    year = yearToday
month = raw_input('Month [%d]:' % (monthToday))
if month.isdigit():
    month = int(month)
else:
    month = monthToday

filesList = glob.glob('*.svg')
if len(filesList) == 0:
    fileHandle = raw_input('Insert calendar template: ')
else:
    i = 0
    print 'Choose calendar template: '
    for j in filesList:
        i = i + 1
        print i, j
    fileHandle = filesList[input('Choice: ') - 1]


calendar.setfirstweekday(calendar.SUNDAY)
calendario = calendar.monthcalendar(year, month)

dom = xml.dom.minidom.parse(fileHandle)

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

targetFile = raw_input('Insert target file name: ')
targetHandle = open(targetFile, 'w')
targetHandle.write(dom.toxml().encode('UTF-8'))
targetHandle.close()
print 'Done!'
