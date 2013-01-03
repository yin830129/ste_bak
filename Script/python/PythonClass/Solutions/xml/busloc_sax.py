import urllib
import xml.sax

class BusHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_bus = {}
        self.current_tag = None
        self.current_text = []

    def startElement(self,name,attrs):
        # If the starting 'bus' is encountered, clear the dict of
        # collected data.
        if name == 'bus':
            self.current_bus = {}
            self.current_tag = None
        else:
            self.current_tag = name
            self.current_text = []

    def characters(self,data):
        # Collect text if curret_tag is set
        if self.current_tag:
            self.current_text.append(data)

    def endElement(self,name):
        # If ending 'bus' is encountered, print out collected data
        if name == 'bus':
            print "%s,%s,%s,%s,%s" % (
                self.current_bus['id'],
                self.current_bus['route'],
                self.current_bus['direction'],
                self.current_bus['latitude'],
                self.current_bus['longitude'])
        else:
            if self.current_tag:
                self.current_bus[self.current_tag] = "".join(self.current_text)
                self.current_tag = None

# Parse the XML
hand = BusHandler()
xml.sax.parse(open("../../Data/allroutes.xml"), hand)
