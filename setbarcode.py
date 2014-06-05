#! /usr/bin/python
#
import ConfigParser


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


def barcodefromconfig(tofile = True):
    config = ConfigParser.RawConfigParser()
    tp = fromfile()

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
        print out


if __name__ == "__main__":
   barcodefromconfig()
