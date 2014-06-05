PaspberryPi-WipeOn-Applictor
============================

Simple wipe on applicator device project based on RaspberryPi and TSC-244 Plus thermal printer

Raspberry has distanse sensor and thermal printer connected. 
When Raspberry got box in range it sends command to print label. 
Box gets to printer and label applis to it.
Some label setting are on webinterface of Raspberry.

file list:
   adm.html - html template of admin page
   adm.py - cgi python scrip of admin page
   lighttpd.conf - example of lighttpd configuration file
   barcode.bas - example output of barcode script to thermal printer
   barcode.template.bas - barcode template to create barcode.bas
   printer.config - example of printer config
   printonkeyborard.py - script prints label to printer on keypressed
   setbarcode.py - script creates barcode.bas from barcode.template using printer.config
   
directory structure:
   /home/pi/barcode.bas
   /home/pi/barcode.template.bas
   /home/pi/printer.config
   /home/pi/printonkeyborard.py
   /home/pi/setbarcode.py
   /var/www/cgi-bin/adm.html
   /var/www/cgi-bin/adm.py
   /etc/lighttpd/lighttpd.conf


To setup web administration page you need to install lighttpd with pyton cgi mod

    sudo apt-get lighttpd
    
Lighttpd config file changes:
    
   #mod_cgi and mod_rewrite shoud be on
   server.modules = (
        "mod_access",
        "mod_alias",
        "mod_compress",
        "mod_redirect",
        "mod_cgi",
        "mod_rewrite",
    )
    
    #rule enables cgi script in /cgi-bin/
    $HTTP["url"] =~ "^/cgi-bin/" {
        cgi.assign = (".py" => "/usr/bin/python")
    }

    #rewrite rule redirects any url to our adm.py cgi script
    url.rewrite-once = (
        "^/$" => "/cgi-bin/adm.py$1",
    )

