#! /usr/bin/python
#
import ConfigParser
import cgi

def chck(frm, name):
    res = ""
    if frm.has_key(name):
        res = frm.getvalue(name)

    return res

def fromfile():
    fp = open('/home/pi/printer.config')
    config = ConfigParser.RawConfigParser()
    config.readfp(fp)
    tp_res = (config.getboolean('main','manual'),
        config.get('main','line'),
        config.get('main','barcode'),
        config.get('main','color'),
        config.get('main','category'),
        "Editing...")
    fp.close()
    return tp_res

def fromform():
    buf = chck(form, "Manual")
    tp_res = (buf == 'on',
        chck(form, "LineNumber"),
        chck(form, "BarCode"),
        chck(form, "Color"),
        chck(form, "Category"),
        "Saved...")
    return tp_res

def savetofile():
    config.add_section('main')
    config.set('main', 'manual',   tp[0])
    config.set('main', 'line',     tp[1])
    config.set('main', 'barcode',  tp[2])
    config.set('main', 'color',    tp[3])
    config.set('main', 'category', tp[4])
    fp = open('/home/pi/printer.config','wb')
    config.write(fp);
    
    
form = cgi.FieldStorage()
config = ConfigParser.RawConfigParser()

print "Content-Type: text/html\n\n"

if len(form) == 0:
    tp = fromfile()
else:
    tp = fromform()
    savetofile()

buf = ""
if tp[0]:
    buf = "checked"

ft = open('/var/www/cgi-bin/hello.html')
str = ft.read()
ft.close()

z = (buf,) + tp[1:3]

cl_d = {"white": ("selected", ""),
    "brown": ("", "selected")}

ct_d = {"C0": ("selected", "", "", "", ""),
    "C1": ("", "selected", "", "", ""),
    "C2": ("", "", "selected", "", ""),
    "CW": ("", "", "", "selected", ""),
    "CM": ("", "", "", "", "selected")}

z = z + cl_d[tp[3]] + ct_d[tp[4]] + (tp[5],)

print str % z
