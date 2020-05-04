import math
from decimal import *
n= 3.14159
r = input()
a = n * float(r)**2
decimal = Decimal(a)
print ("A="+str(round(decimal, 4)))
