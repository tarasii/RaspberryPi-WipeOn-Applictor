#! /usr/bin/python
#
import configadapter
import cgi
import os

cl_d = {"white": ("selected", ""),
    "brown": ("", "selected")}

ct_d = {"C0": ("selected", "", "", "", ""),
    "C1": ("", "selected", "", "", ""),
    "C2": ("", "", "selected", "", ""),
    "CW": ("", "", "", "selected", ""),
    "CM": ("", "", "", "", "selected")}

cz_d = {"barcode":("selected",""),
    "fixed":("","selected")}

def chck(frm, name, default = ""):
    res = default
    if frm.has_key(name):
        res = frm.getvalue(name)

    return res

def fromform():
    buf = chck(form, "manual")
    tp_res = (buf == 'on',
        chck(form, "lineNumber",tp[1]),
        chck(form, "barCode",   tp[2]),
        chck(form, "color",     tp[3]),
        chck(form, "category",  tp[4]),
        chck(form, "enterprise",tp[5]),
        chck(form, "template",  tp[6]),
        chck(form, "barcode2",  tp[7]),
        chck(form, "category2", tp[8]),
        chck(form, "number",    tp[9]),
        tp[10],
        "Saved...")
    return tp_res
    
form = cgi.FieldStorage()

print "Content-Type: text/html\n\n"

tp = configadapter.fromfile()
if len(form) != 0:
    tp = fromform(tp)
    configadapter.savetofile(tp)

buf = ""
if tp[0]:
    buf = "checked"

str = ""
with open('/var/www/cgi-bin/adm.html') as ft:
     str = ft.read()

#flog = '/home/pi/prnt.log'
#lf = 0
#if os.path.exists(flog):
#    with open(flog,'r') as fl:
#        lf = len(fl.readlines())

z = (buf,) + (tp[1], tp[5],)+ cz_d[tp[6]] + cl_d[tp[3]] + ct_d[tp[4]] + (tp[2],) + ct_d[tp[8]] + (tp[7], tp[9], tp[11], tp[10])

if str=="":
    print z
else:
    print (str % z)
