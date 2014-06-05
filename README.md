PaspberryPi-WipeOn-Applictor
============================

Simple wipe on applicator device project based on RaspberryPi and TSC-244 Plus thermal printer

The Raspberry has distanse sensor and a thermal printer connected. 
When the Raspberry got a box in range it sends command to print a label. 
When a box gets close to printer then the label applies to it.
Some label setting are on the webinterface of Raspberry.

file list:

    adm.html             - html template of admin page
    adm.py               - cgi python scrip of admin page
    lighttpd.conf        - example of lighttpd configuration file
    barcode.bas          - example output of barcode script to thermal printer
    barcode.template.bas - barcode template to create barcode.bas
    printer.config       - example of printer config
    printonkeyborard.py  - script prints label to printer on keypressed
    setbarcode.py        - script creates barcode.bas from barcode.template using printer.config
   
directory structure:

    /home/pi/
        barcode.bas
        barcode.template.bas
        printer.config
        printonkeyborard.py
        setbarcode.py
    /var/www/cgi-bin/
        adm.html
        adm.py
    /etc/lighttpd/
        lighttpd.conf

The adm.py script writes printer.config file. 
Params from this config file used by setbarcode.py script to create barcode.bas from barcode.template.bas.
The printonkeyboard.py script calls setbarcode.py to create fresh barcode.bas and sends it to a printer.


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

http://mike632t.wordpress.com/2013/09/21/installing-lighttpd-with-python-cgi-support/
