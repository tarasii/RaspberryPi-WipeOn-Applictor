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
def TableElement(eltype, tp, attr = ""):
   res = ""
   if not tp:
      tp = ("",)


   if isinstance(tp, basestring):
      res = tp
   elif isinstance(tp, (list, tuple)):
      for el in tp:
         res = res + el

   patern = "<%s%s>%s</%s>\n"
   return patern % (eltype, attr, res, eltype)

def TableCell(tp, cs=0):
   attr = ""
   if cs!=0:
      attr = " colspan = %s" % cs
 
   return TableElement("td", tp, attr)

def TableRow(tp=""):
   return TableElement("tr", tp)

def TableLine(tp=""):
   return TableRow(tp)

def TableHead(tp=""):
   return TableElement("th", tp)

def Table(tp="",border=0):
   attr = " width=100% cellspacing=1"
   if border!=0:
      attr = attr + " border=%s" % border
   return TableElement("table", tp, attr)

def TD(tp="", cs=0):
   return TableCell(tp, cs)

def TR(tp=""):
   return TableRow(tp)

def TH(tp=""):
   return TableHead(tp)

#tables>>



def Form(tp):
   res = "<form name=settings method=post>\n"
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = res + tp
   elif isinstance(tp, (list, tuple)):
      for el in tp:
         res = res + el
      
   res = res + "</form>"
   return res

def Html(name, tp):
   res = "Content-Type: text/html\n\n"
   res = res + "<html>\n<head>\n<meta content=text/html; charset=UTF-8 />\n"
   res = res + "<title>%s</title>\n" % (name,)
   
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = res + tp
   elif isinstance(tp, (list, tuple)):
      for el in tp:
         res = res + el
   
   res = res + "</body>\n</html>"
   return res
