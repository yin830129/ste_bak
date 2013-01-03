# follow.py

import time
import os

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    with open(filename,"r") as f:
        f.seek(0,os.SEEK_END)
        while True:
             line = f.readline()
             if line != '':
                 yield line
             else:
                 time.sleep(0.1)    # Sleep briefly to avoid busy wait

def splitter(lines):
    '''
    Split a sequence of lines containing CSV data into a sequence of rows.
    '''
    for line in lines:
        yield line.split(',')

def make_records(rows,names):
    '''
    Turn a sequence of rows into a sequence of dictionaries.
    '''
    for row in rows:
        yield dict(zip(names,row))

def unquote(records,keylist):
    '''
    Unquote the value of selected keys in a sequence of dictionaries.
    '''
    for r in records:
        for key in keylist:
            r[key] = r[key].strip('"')
        yield r

def convert(records,converter,keylist):
    '''
    Apply type conversion to the value of selected keys in a sequence of dictionaries.
    '''
    for r in records:
        for key in keylist:
            r[key] = converter(r[key])
        yield r

def parse_stock_data(lines):
    '''
    Take a sequence of lines and produce a sequence of dictionaries containing stock market data.
    '''
    rows = splitter(lines)
    records = make_records(rows,['name','price','date','time',
                              'change','open','high','low','volume'])
    records = unquote(records,["name","date","time"])
    records = convert(records,float,['price','change','open','high','low'])
    records = convert(records,int,['volume'])
    return records

# Sample code for following the real-time log
if __name__ == '__main__':
    lines = follow("../../Data/stocklog.dat")
    records  = parse_stock_data(lines)
    for r in records:
        print "%(name)10s %(price)10.2f %(change)10.2f %(volume)10d" % r
