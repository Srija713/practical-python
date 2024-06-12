# pcost.py
#
# Exercise 1.27
cost=0
with open('Data/portfolio.csv', 'rt') as f:
    header=next(f)
    for line in f:
        li=line.split(',')
        cost=cost+(float(li[1])*float(li[2]))
print("Total cost",cost)
f.close()

