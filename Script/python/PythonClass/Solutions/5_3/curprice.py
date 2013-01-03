# curprice.py

# A dynamically updated price object.   This very minimally looks
# like a dictionary

import urllib

class CurrentPrices(object):
    '''
    An object that returns current stock prices when accessed as a mapping.
    '''
    def __getitem__(self,name):
        request = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1&e=.csv" % name
        u = urllib.urlopen(request)
        price = float(u.read())
        return price
