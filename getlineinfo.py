#! /usr/bin/python
#
import json

def readfromjson():
    json_data=open('config.json')
    data = json.load(json_data)
    json_data.close()
    return (data[0],data[1])

def readfromconfig():
    import configadapter
    tp = configadapter.fromfile()
    #tp = ("","01L","")
    return (str(int(tp[1][:2])),tp[1][2:])

def readlineinfo(readtype = 'config'):
    if readtype == 'config':
        tpc = readfromconfig()
    else:
        tpc = readfromjson()
    
    json_data=open('maxln.json')
    data = json.load(json_data)
    json_data.close()

    for curln in data:
        if tpc[0] == curln[1]:
            return (tpc[0], tpc[1], curln[3], curln[2])
    return (tpc[0], tpc[1], "","")

if __name__ == "__main__":
    tp = readlineinfo()
    print (tp)
    
