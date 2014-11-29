#! /usr/bin/python
#
from myhtml import *

print Html("My html test",
   Form("Myhtmltest.py",
        Header("My html test"),
        Paragraph("Hello world!"), 
        Table(TableHead("N","Name","Surname","Mark"), #TR(TH("N"),TH("Name"),TH("Surname"),TH("Mark"),""),
          TR(TD("1."), TD("John"),    TD("Doe"),       TD(Input("tst1")),""),
          TR(TD("2."), TD("Michael"), TD("Cooperman",  "cs=2"),""),
          TR(TD("3."), TD("Mark"),    TD("Lieberman"), TD(Input("tst3")),""),
          TR(TD("4."), TD("Alex"),    TD("Miller"),    TD(Input("tst4")),""),
          {"cs":1,"br":1} #"cs=1 br=1"
          ),
        HyperLink("google.com"),
        NL(),
        NL(),
        CheckBox("manual", True),
        NL(),
        TextBox("test","111"),
        BR(),
        SubmitButton("save"),
        CancelButton("cancel"),
        ""
       )
   )
