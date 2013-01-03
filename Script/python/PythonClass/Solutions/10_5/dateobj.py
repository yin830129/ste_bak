# dateobj.py
import time

class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def format(self):
        return "%d-%d-%d" % (self.year, self.month, self.day)
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)
