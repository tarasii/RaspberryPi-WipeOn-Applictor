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

def Input(name, val="", disabled=False):
   strdis = ""
   strval = ""
   if disabled:
      strdis = " disabled"
   if val:
      strval = " value="
   patern = "<input name=%s%s%s%s>\n"
   return patern % (name, strdis, strval, val)

def TextBox(name, val, disabled=False):
   return Label(name+": ")+Input(name,val,disabled)


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
def TableElement(eltype, tp):
   res = ""
   attr = ""

   #print tp
   #print eltype
   #return ""
   ttp = TupleToString(tp)
   res = ttp[0]
   attr = ttp[1]

   eltype.lower()
   if eltype.startswith("td"):
      attr = attr.replace("cs=","colspan=")
   elif eltype.startswith("table"):
      attr = attr.replace("cs=","cellspacing=")
      attr = attr.replace("br=","border=")
      attr = attr.replace("wd=","width=")

   if (not attr.startswith(" ")) and (attr):
      attr = " "+attr
 
   patern = "<%s%s>%s</%s>\n"
   return patern % (eltype, attr, res, eltype)

def TableCell(tp, cs=0):
   return TableElement("td", tp)

def TableRow(*tp):
   return TableElement("tr", tp)

def TableLine(*tp):
   return TableElement("tr", tp)

def TableHead(*tp):
   return TableElement("th", tp)

def Table(*tp):
   return TableElement("table", tp)

def TD(*tp):
   return TableElement("td", tp)

def TR(*tp):
   return TableElement("tr", tp)

def TH(*tp):
   return TableElement("th", tp)

#tables>>


def DictToString(dt):
   res = ""
   if not dt:
      res = ""
   elif isinstance(dt, basestring):
      res = dt
   elif isinstance(dt, dict):
      for el in dt:
         res = res + "".join((" ", el, "=", str(dt[el])))

   return res

def TupleToString(tp):
   res = ""
   attr = ""
   if not tp:
      res = ""
   elif isinstance(tp, basestring):
      res = tp
   elif isinstance(tp, (list, tuple)):
      if len(tp)>1:
         res = "".join(tp[:-1])
         attr = DictToString(tp[-1])
      else:
         res = "".join(tp)

   return (res, attr)

def Form(name, *tp):
   ttp = TupleToString(tp)
   #print ttp
   res = "<form name=%s method=post%s>\n %s </form>" % (name,ttp[1],ttp[0])
   return res

def Html(name, *tp):
   ttp = TupleToString(tp)
   res = "Content-Type: text/html\n\n"
   res = res + "<html>\n<head>\n<meta content=text/html; charset=UTF-8 />\n"
   res = res + "<title>%s</title>\n<body>\n%s\n</body>\n</html>" % (name,ttp[0])
   return res

if __name__ == "__main__":
   print(Html("MyHtml module test",Form("myhtml.py", Header("My Html"),Label("Students assessment:"), 
      Table(TR(TH("N"),TH("Name"),TH("Surname"),TH("Mark"),""),
            TR(TD("1."),TD("John"),TD("Doe"),TH(Input("tst1")),""),
            TR(TD("2."),TD("Michael"),TD("Cooperman","cs=2"),""),
            TR(TD("3."),TD("Mark"),TD("Lieberman"),TH(Input("tst3")),""),
            TR(TD("4."),TD("Alex"),TD("Miller"),TH(Input("tst4")),""),
      "cs=1 br=1"),HyperLink("google.com"),"")))
