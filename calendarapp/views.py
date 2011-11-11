from django.http import HttpResponse
from calendario import render_calendar
import xml.dom.minidom
import os.path

APP_ROOT=os.path.realpath(os.path.dirname(__file__))

def render(request, name, year, month):
    filename = os.path.join(APP_ROOT, "static/calendars/%s.svg" % name)
    dom = render_calendar(xml.dom.minidom.parse(filename), int(month), int(year))

    return HttpResponse(dom.toxml().encode('utf8'), mimetype="image/svg+xml")

def renderpdf(request, name, year, month):
    import subprocess

    filename = os.path.join(APP_ROOT, "static/calendars/%s.svg" % name)
    dom = render_calendar(xml.dom.minidom.parse(filename), int(month), int(year))

    svghandle = open("tmp.svg", "w")
    svghandle.write(dom.toxml().encode("utf8"))
    svghandle.close()

    retcode = subprocess.call(['inkscape', '-A', 'tmp.pdf', 'tmp.svg'])

    if retcode == 0:
        pdfhandle = open("tmp.pdf", "r")
        pdfcontent = pdfhandle.read()
        pdfhandle.close()

        return HttpResponse(pdfcontent, mimetype="application/pdf")
    else:
        return HttpResponse(":(")
