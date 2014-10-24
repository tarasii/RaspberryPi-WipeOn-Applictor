DAY = %s
MONTH = %s
YEAR = %s
UPBAR$ = "%s"
EGG$ = "%s"
EGGC$ = "%s"
LNUM$ = "%s"
ENT$ = "%s"
ID$ = "%06d"
SIZE 100 mm, 80 mm
CLS
BARCODE 90, 50, "EAN13", 80,  0, 90, 6, 0, UPBAR$
#BARCODE 630, 650, "128", 120,  1, 270, 4, 3, ""+ENT$+LNUM$+EGG$+EGGC$+FORMAT$(NOW$(),"yyyymmdd")
BARCODE 630, 650, "128", 120,  1, 270, 4, 3, ""+ENT$+LNUM$+EGG$+EGGC$+ID$
TEXT 340, 630, "2", 270, 1, 1, ""+FORMAT$(NOW$(),"yyyy/mm/dd")
TEXT 340, 400, "2", 270, 1, 1, ""+LNUM$
TEXT 340, 230, "2", 270, 1, 1, ""+EGG$
TEXT 340, 100, "2", 270, 1, 1, "360"
PUTBMP 100, 5, "P003.BMP"
PRINT 1
EOP
