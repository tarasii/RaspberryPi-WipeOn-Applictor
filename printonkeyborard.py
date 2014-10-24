#! /usr/bin/python
#
import sys
import tty, termios
import printlabel

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

printlabel.printlabel()

while True:
    ch = getch()
    if ch == 'q':
        break;

    #print ch
    printlabel.printlabel()        
