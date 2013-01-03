# mortgage.py

principal = 500000.00    # Mortgage amount
rate = 0.04              # Interest rate
payment = 499            # Monthly payment
month = 0
totalpaid=0

while principal > 0:
    principal = principal*(1+rate/12) - payment
    totalpaid+=payment
    month =month+1
    print month,totalpaid,principal
    if month == 24:
        rate=0.09
        payment=3999
        
        
print month,totalpaid        
