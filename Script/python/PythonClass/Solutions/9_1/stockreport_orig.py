# stockreport.py

import sys
import urllib
import csv

if len(sys.argv) != 2:
    print >>sys.stderr,"Usage: %s symbol" % sys.argv[0]
    raise SystemExit(1)

symbol = sys.argv[1]

u      = urllib.urlopen("http://download.finance.yahoo.com/d/quotes.csv?f=snl1d1t1c1p2ohgv&s="+symbol)
colnames = ['symbol','name','price','date','time','change','percent','open','high','low','volume']
stocks = csv.DictReader(u,colnames)

for s in stocks:
    print "<p>"
    print "<b>%s (%s)</b><br>" % (s['symbol'],s['name'])
    print "<font size=+2><b>%s</b></font>" % (s['price'])
    print "%s (%s)" % (s['change'],s['percent'])
    print "%s %s<br>" % (s['date'], s['time'])
    print "<table>"
    print "<tr>"
    print "<td>Open:</td><td>%s</td><td>Volume:</td><td>%s</td>" % (s['open'],s['volume'])
    print "</tr>"
    print "<tr>"
    print "<td>High:</td><td>%s</td><td>Low:</td><td>%s</td>" % (s['high'],s['low'])
    print "</table>"
    print "</p>"

