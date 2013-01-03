# stockreport.py

import sys
import urllib
import csv
import string

if len(sys.argv) != 2:
    print >>sys.stderr,"Usage: %s symbol" % sys.argv[0]
    raise SystemExit(1)

symbol = sys.argv[1]
output = string.Template(open("stockreport_template.html").read())

u      = urllib.urlopen("http://download.finance.yahoo.com/d/quotes.csv?f=snl1d1t1c1p2ohgv&s="+symbol)
colnames = ['symbol','name','price','date','time','change','percent','open','high','low','volume']
stocks = csv.DictReader(u,colnames)

for s in stocks:
    print output.substitute(s)

