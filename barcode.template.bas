DAY = %s
MONTH = %s
YEAR = %s
UPBAR$ = "%s"
EGG$ = "%s"
EGGC$ = "%s"
LNUM$ = "%sL"
ENT$ = "%s"
SIZE 100 mm, 80 mm
CLS
BARCODE 90, 50, "EAN13", 80,  0, 90, 6, 0, UPBAR$
BARCODE 630, 650, "128", 80,  1, 270, 3, 2, ""+ENT$+"0"+LNUM$+EGG$+EGGC$+FORMAT$(NOW$(),"yyyymmdd")
TEXT 340, 630, "2", 270, 1, 1, ""+FORMAT$(NOW$(),"yyyy/mm/dd")
TEXT 340, 400, "2", 270, 1, 1, ""+LNUM$
TEXT 340, 230, "2", 270, 1, 1, ""+EGG$
TEXT 340, 100, "2", 270, 1, 1, "360"
PUTBMP 100, 5, "P009.BMP"
PRINT 1
EOP
