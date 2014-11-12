#! /usr/bin/python
#
import myhtml

print myhtml.Html("test",
   (myhtml.Form(
       (myhtml.CheckBox("manual", True),
        myhtml.NL(),
        myhtml.TextBox("test","111"),
        myhtml.NL(),
        myhtml.SubmitButton("save"),
        myhtml.CancelButton("cancel"),
       )),
   ))
