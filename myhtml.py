#! /usr/bin/python
#

def Label(name):
   patern = "<a>%s</a>\n"
   return patern % (name, )

def Paragraph(txt):
   patern = "<p>%s</p>\n"
   return patern % (txt,)

def Header(txt):
   patern = "<h1>%s</h1>\n"
   return patern % (txt,)

def SubmitButton(name):
   patern = "<input type=submit value=%s>\n"
   return patern % (name, )

def CancelButton(name):
   patern = "<input type=reset value=%s>\n"
   return patern % (name, )

def Input(name, val=""):
   patern = "<input name=%s value=%s>\n"
   return patern % (name, val)

def TextBox(name, val):
   return Label(name+": ")+Input(name,val)

def TextBox(name, val):
   return Label(name+": ")+Input(name,val)

def HyperLink(link, text=""):
   pref = "http://"
   if not text:
      text = link.replace(pref,"")

   if link.lower().find(pref)==-1:
      link = pref + link
 
   patern = "<a href=%s>%s</a>\n"
   return patern % (link, text)

def InputCheckBox(name, ch = False):
   chtxt = ""
   if ch : chtxt = "checked"
   patern = "<input type=checkbox name=%s %s>\n"
   return patern % (name, chtxt)

def CheckBox(name, ch = False):
   return InputCheckBox(name, ch)+Label(name)

def NL():
   return "<br>\n"

def BR():
   return NL()

#<<tables   
def TableElement(eltype, attr, tp):
   res = ""
   res = res + CheckTuple(tp)
   if not attr.startswith(" "):
      attr = " "+attr
 
   patern = "<%s%s>%s</%s>\n"
   return patern % (eltype, attr, res, eltype)

def TableCell(tp, cs=0):
   attr = ""
   if cs!=0:
      attr = " colspan = %s" % cs
 
   return TableElement("td", attr, tp)

def TableRow(tp=""):
   return TableElement("tr", "", tp)

def TableLine(tp=""):
   return TableRow(tp)

def TableHead(tp=""):
   return TableElement("th", "", tp)

def Table(attr = "", *tp):
   #attr = " width=100% cellspacing=1"
   attr.lower()
   if attr.find("cellspacing")==-1:
       attr = attr + " cellspacing=1"
   
   #if border:
   #   attr = attr + " border=%s" % border
   #
   #if width:
   #   attr = attr + " width=" + width
   #for param in tp
   #   if isinstance(param, dict):   

   return TableElement("table", attr, tp)

def TD(*tp):
   #return TableCell(tp, cs)
   return TableCell(tp)

def TR(*tp):
   return TableRow(tp)

def TH(*tp):
   return TableHead(tp)

#tables>>

def CheckTuple(tp):
   res = ""
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = res + tp
   elif isinstance(tp, (list, tuple)):
      for el in tp:
         res = res + el
   
   return res

def Form(name, *tp):
   res = "<form name=%s method=post>\n" % (name,)
   res = res + CheckTuple(tp)
   res = res + "</form>"
   return res

def Html(name, *tp):
   res = "Content-Type: text/html\n\n"
   res = res + "<html>\n<head>\n<meta content=text/html; charset=UTF-8 />\n"
   res = res + "<title>%s</title>\n" % (name,)
   res = res + CheckTuple(tp)
   res = res + "</body>\n</html>"
   return res
