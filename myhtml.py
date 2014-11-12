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

def InputCheckBox(name, ch = False):
   chtxt = ""
   if ch : chtxt = "checked"
   patern = "<input type=checkbox name=%s %s>\n"
   return patern % (name, chtxt)

def CheckBox(name, ch = False):
   return InputCheckBox(name, ch)+Label(name)

def NL():
   return "<br>\n"

def Form(tp):
   res = "<form name=settings method=post>\n"
   #ln = len(tp)
   for el in tp:
      res = res + el
   
   res = res + "</form>"
   return res

def Html(name, tp):
   res = "Content-Type: text/html\n\n"
   res = res + "<html>\n<head>\n<meta content=text/html; charset=UTF-8 />\n"
   res = res + "<title>%s</title>\n" % (name,)
   #ln = len(tp)
   for el in tp:
      res = res + el
   
   res = res + "</body>\n</html>"
   return res
