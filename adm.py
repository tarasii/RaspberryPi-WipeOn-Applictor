#! /usr/bin/python
#
import ConfigParser
import cgi

cl_d = {"white": ("selected", ""),
    "brown": ("", "selected")}

ct_d = {"C0": ("selected", "", "", "", ""),
    "C1": ("", "selected", "", "", ""),
    "C2": ("", "", "selected", "", ""),
    "CW": ("", "", "", "selected", ""),
    "CM": ("", "", "", "", "selected")}

def chck(frm, name, default = ""):
    res = default
    if frm.has_key(name):
        res = frm.getvalue(name)

    return res

def chckc(cnf, name, default = ""):
    res = default
    if cnf.has_option('main',name):
        if name == "manual":
            res = cnf.getboolean('main',name)
        else:
            res = cnf.get('main',name)

    return res

def fromfile():
    fname = '/home/pi/printer.config';
    tp_def = (False,"00","000000000000","white","C0","XXX","Editing...")
    if not os.path.isfile(fname):
        return tp_def

    fp = open('/home/pi/printer.config')
    config = ConfigParser.RawConfigParser()
    config.readfp(fp)
    tp_res = (chckc(config,'manual',tp_def[0]),
        chckc(config,'line',       tp_def[1]),
        chckc(config,'barcode',    tp_def[2]),
        chckc(config,'color',      tp_def[3]),
        chckc(config,'category',   tp_def[4]),
        chckc(config,'enterprise', tp_def[5]),
        tp_def[6])
    fp.close()
    return tp_res

def fromform():
    buf = chck(form, "Manual")
    tp_res = (buf == 'on',
        chck(form, "LineNumber"),
        chck(form, "BarCode"),
        chck(form, "Color"),
        chck(form, "Category"),
        chck(form, "enterprise"),
        "Saved...")
    return tp_res

def savetofile():
    config.add_section('main')
    config.set('main', 'manual',     tp[0])
    config.set('main', 'line',       tp[1])
    config.set('main', 'barcode',    tp[2])
    config.set('main', 'color',      tp[3])
    config.set('main', 'category',   tp[4])
    config.set('main', 'enterprise', tp[5])
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

ft = open('/var/www/cgi-bin/adm.html')
str = ft.read()
ft.close()

z = (buf,) + tp[1:3] + cl_d[tp[3]] + ct_d[tp[4]] + (tp[5], tp[6])

print str % z
