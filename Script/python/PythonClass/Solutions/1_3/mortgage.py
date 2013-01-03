# mortgage.py
principal  = 500000.00
rate       = 0.04
payment    = 499.00

months     = 0
total_paid = 0.00

while principal > 0:
      principal = principal*(1+rate/12) - payment
      total_paid += payment
      months += 1
      if months == 24:
           payment = 3999.00
           rate    = 0.09
      # print months,total_paid,principal    (Uncomment for part b)

print "Total months", months
print "Total paid", total_paid
