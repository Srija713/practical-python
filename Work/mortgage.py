# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=0
extra_payment_start_month = 0
extra_payment_end_month = 12
extra_payment = 1000

while principal > 0:
    if months==extra_payment_start_month:
        for i in range(extra_payment_end_month-extra_payment_start_month):
            principal = principal * (1+rate/12) - (payment+extra_payment)
            total_paid = total_paid + payment+extra_payment
            months=months+1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months=months+1

print('Total paid', total_paid,'months:',months)