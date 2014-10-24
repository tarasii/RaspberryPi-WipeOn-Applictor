#! /usr/bin/python
#
import configadapter
from datetime import datetime
import sqlite3

fdb = '/home/pi/print.db'

def barcodefromconfig(scnd = False, tofile = True):
    tp = configadapter.fromfile()

    ft = open('/home/pi/barcode.template.bas')
    str = ft.read()
    ft.close()

    cl_d = {"white": "W",
        "brown": "B"}

    #get id for new barcode from db
    conn = sqlite3.connect(fdb)
    c = conn.cursor()
    c.execute('select max(id) from printid')
    r = c.fetchone()
    if r[0]:
       id = r[0]+1
    else: id = 1
    
    conn.close()

    dt = datetime.now()

    if (scnd == True):
        z = (dt.day, dt.month, dt.year, tp[7],  tp[8], cl_d[tp[3]], tp[1], tp[5], id)
    
    else:    
        z = (dt.day, dt.month, dt.year, tp[2],  tp[4], cl_d[tp[3]], tp[1], tp[5], id)

    out = str % z

    if tofile:
        fd = open('/home/pi/barcode.bas','wb')
        fd.write(out)
        fd.close()
    else:
        print (out)


if __name__ == "__main__":
   barcodefromconfig()
