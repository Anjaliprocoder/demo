#user defined functions
import mod
import math
import datetime
print(mod.add(5,6))
print(mod.sub(3,1))
print(mod.mul(1,2))
print(mod.div(6,2))
#built in mathematical functions
print(min(1,2,3,4))
print(max(1,2,3,4))
print(abs(-4))
print(pow(4,2))
#module based math functions
print(math.pi)
print(math.sqrt(9))
print(math.ceil(5.3))
print(math.floor(5.3))
print(math.factorial(2))

#datetime modules
a=datetime.datetime.now()
print(a)
#legal format code for extracting particular day,month likewise
print(a.strftime("%A"))#day corresponding
print(a.strftime("%a"))
print(a.strftime("%B"))#month
print(a.strftime("%b"))
print(a.strftime("%Y"))#year
print(a.strftime("%y"))
print(a.strftime("%H"))#hour
print(a.strftime("%M"))#minute
b=datetime.datetime(2000,6,18)
print(b.strftime("%A"))







