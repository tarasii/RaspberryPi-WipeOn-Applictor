#! /usr/bin/python
#
import sqlite3
import setbarcode
import os
import shutil

fdev = '/dev/usb/lp0'
#flog = '/home/pi/prn.log'
fdb = '/home/pi/print.db'
fbar = '/home/pi/barcode.bas'

def printlabel(scnd = False):
    conn = sqlite3.connect(fdb)
    c = conn.cursor()

    noerr = 0
    bar = setbarcode.barcodefromconfig(scnd)
    if os.path.exists(fdev):
        shutil.copy(fbar, fdev)
        str = "print "
        c.execute("INSERT INTO printid(barcode) VALUES (?)",(bar,))

    else:
        str = "error "
        noerr = 1

    c.execute("INSERT INTO printlog(comment,err) VALUES (?,?)",(str,noerr,))
    
    #str = str + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ") + bar + "\n"
    #with open(flog,'a') as fl:
    #    fl.write(str)

    conn.commit()

    conn.close()
    return


if __name__ == "__main__":
    printlabel()
