#! /usr/bin/python
#
import ConfigParser
import os

#fname = '/home/pi/printer.config';
fname = 'printer.config';
config = ConfigParser.RawConfigParser()

def chckc(cnf, name, default = ""):
    res = default
    if cnf.has_option('main',name):
        if name == "manual":
            res = cnf.getboolean('main',name)
        else:
            res = cnf.get('main',name)

    return res

def fromfile():
    tp_def = (False,"00","000000000000","white","C0","XXX","Editing...")
    if not os.path.isfile(fname):
        return tp_def

    fp = open(fname)
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

def savetofile(tp):
    config.add_section('main')
    config.set('main', 'manual',     tp[0])
    config.set('main', 'line',       tp[1])
    config.set('main', 'barcode',    tp[2])
    config.set('main', 'color',      tp[3])
    config.set('main', 'category',   tp[4])
    config.set('main', 'enterprise', tp[5])
    fp = open(fname,'wb')
    config.write(fp);
    

if __name__ == "__main__":
    tp = fromfile()
    print (tp)
    
