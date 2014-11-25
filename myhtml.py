#! /usr/bin/python
#

def Label(name):
   patern = "<a>%s<a/>\n"
   return patern % (name, )

def SubmitButton(name):
   patern = "<input type=submit value=%s>\n"
   return patern % (name, )

def CancelButton(name):
   patern = "<input type=reset value=%s>\n"
   return patern % (name, )

def Input(name, val):
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
<<<<<<< HEAD
 
=======

>>>>>>> 9c66feb5c80bf810117f50747453e26958cb1df3
   patern = "<a href=%s>%s</a>\n"
   return patern % (link, text)

def CheckBox(name, ch = False):
   return InputCheckBox(name, ch)+Label(name)

def NL():
   return "<br>\n"

#<<tables   
def TableElement(eltype, tp):
   res = ""
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = tp
   elif isinstance(lst, (list, tuple)):
      for el in tp:
         res = res + el
<<<<<<< HEAD

   patern = "<%s>%s</%s>\n"
   return patern % (eltype, res, eltype)

=======

   for el in tp:
      res = res + el
   patern = "<%s>%s</$s>\n"
   return patern % (elytpe, res, eltype)

>>>>>>> 9c66feb5c80bf810117f50747453e26958cb1df3
def TabelCell(tp):
   return TableElement("td", tp)

def TabelRow(tp):
   return TableElement("tr", tp)

def TabelHeader(tp):
   return TableElement("th", tp)
#tables>>

def Form(tp):
   res = "<form name=settings method=post>\n"
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = tp
   elif isinstance(lst, (list, tuple)):
      for el in tp:
         res = res + el
<<<<<<< HEAD
      
=======

>>>>>>> 9c66feb5c80bf810117f50747453e26958cb1df3
   res = res + "</form>"
   return res

def Html(name, tp):
   res = "Content-Type: text/html\n\n"
   res = res + "<html>\n<head>\n<meta content=text/html; charset=UTF-8 />\n"
   res = res + "<title>%s</title>\n" % (name,)
<<<<<<< HEAD
   
=======

>>>>>>> 9c66feb5c80bf810117f50747453e26958cb1df3
   if not tp:
      tp = ("",)

   if isinstance(tp, basestring):
      res = tp
   elif isinstance(lst, (list, tuple)):
      for el in tp:
         res = res + el
<<<<<<< HEAD
   
=======

>>>>>>> 9c66feb5c80bf810117f50747453e26958cb1df3
   res = res + "</body>\n</html>"
   return res
