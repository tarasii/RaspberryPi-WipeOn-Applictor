import xml.etree.ElementTree as ET
import json

def pars_product_property(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}Name':
            #print ('    ',child.tag, child.text)
            if child.text in ['C0','C0+','C1','C2']:
                ln[3] = child.text
            elif child.text in ['ROBOT-KVOCHKA','Квочка Е3810']:
                ln[3] = "QUO"
            #elif child.text == 'konets mashiny':
            #    ln[3] = "END"
            else:
                ln[3] = "---"

def pars_supply_egg(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}Type':
            #print ('    ',child.tag, child.text)
            if child.text == 'коричневое':
                ln[2] = 'B'

            if child.text == 'белое':
                ln[2] = 'W'
                
            #ln[2] = child.text


def pars_general(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}LaneNumber':
            #print ('    ',child.tag, child.text)
            ln[1] = child.text

        if child.tag == '{omlNamespace}StartDateTime':
            #print ('    ',child.tag, child.text)
            ln[0] = child.text

def pars_supply(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}Egg':
            pars_supply_egg(child, ln)

def pars_product(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}Property':
            pars_product_property(child, ln)

def pars_lanes(elem, ln):
    for child in elem: 
        if child.tag == '{omlNamespace}General':
            pars_general(child, ln)
            
        if child.tag == '{omlNamespace}Supply':
            pars_supply(child, ln)

        if child.tag == '{omlNamespace}Product':
            pars_product(child, ln)

def add_lanes(maxln, ln):
    fnd = False
    print(ln)
    for curln in maxln:
        if ln[1] == curln[1]:
            curln[0] = ln[0]
            curln[2] = ln[2]
            curln[3] = ln[3]
            fnd = True;
            
    if not fnd:
        newln = [ln[0], ln[1], ln[2], ln[3]]
        maxln.append(newln)

def getmobalineinfo(tofile = True)
    tree = ET.parse('LaneActual.xml')
    root = tree.getroot()
    #print (root.tag, root.attrib)
    ln = ["","","",""]
    maxln = []

    cnt = 0
    for child in root:
        cnt = cnt + 1
        #print (child.tag)
        if child.tag == '{omlNamespace}Lane':
            pars_lanes(child, ln);
            add_lanes(maxln, ln)

        #if cnt==90: break


    if tofile:
        with open('maxln.json', 'w') as outfile:
            json.dump(maxln,outfile)
    else:
        print()
        for curln in maxln:
            print (curln)

if __name__ == "__main__":
    getmobalineinfo()
    
