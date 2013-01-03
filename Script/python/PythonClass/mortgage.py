# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\hewu\.spyder2\.temp.py
"""
# mortage.py

principal=500000.00
rate=0.04
payment=499
month=0
totalpaid=0.0

while principal>0:
    principal=principal*(1+rate/12)-payment
    totalpaid+=payment
    month=month+1
    print month,totalpaid,principal
    if month == 24:
        rate=0.09
        payment=3999
print "total paid",totalpaid
print "total month", month
