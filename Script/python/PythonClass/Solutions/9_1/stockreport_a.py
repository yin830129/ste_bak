# stockreport.py

import sys
import urllib
import csv
import string

output = string.Template("""
<p>
<b>$symbol ($name)</b><br>
<font size=+2><b>$price</b></font> 
change ($percent)
$date $time<br>
<table>
   <tr>
      <td>Open:</td><td>$open</td><td>Volume:</td><td>$volume</td>
   </tr>
   <tr>
      <td>High:</td><td>$high</td><td>Low:</td><td>$low</td>
   </tr>
</table>
</p>
""")

if len(sys.argv) != 2:
    print >>sys.stderr,"Usage: %s symbol" % sys.argv[0]
    raise SystemExit(1)

symbol = sys.argv[1]

u      = urllib.urlopen("http://download.finance.yahoo.com/d/quotes.csv?f=snl1d1t1c1p2ohgv&s="+symbol)
colnames = ['symbol','name','price','date','time','change','percent','open','high','low','volume']
stocks = csv.DictReader(u,colnames)

for s in stocks:
    print output.substitute(s)

