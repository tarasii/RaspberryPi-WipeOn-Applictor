#! /usr/bin/python
#
import configadapter
from datetime import datetime

def barcodefromconfig(tofile = True):
    tp = configadapter.fromfile()

    ft = open('/home/pi/barcode.template.bas')
    str = ft.read()
    ft.close()

    cl_d = {"white": "W",
        "brown": "B"}

    dt = datetime.now()

    z = (dt.day, dt.month, dt.year, tp[2],  tp[4], cl_d[tp[3]], tp[1], tp[5])

    out = str % z

    if tofile:
        fd = open('/home/pi/barcode.bas','wb')
        fd.write(out)
        fd.close()
    else:
        print (out)


if __name__ == "__main__":
   barcodefromconfig()
