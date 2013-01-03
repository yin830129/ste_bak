# follow.py
import os
import time

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

# Example use
if __name__ == '__main__':
    for line in follow("../../Data/stocklog.dat"):
        row = line.split(",")
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        print "%10s %10s %10s" % (name,price,change)
