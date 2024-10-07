#for validation when module is used
#module re-search(to search whether the given pattern is matched),split(for splitting),sub(substituting) are regular expression module functions
#meta characters[]-set of characters,.-any character,^-starts with,$-ends with,*-zero or more occurrence,
# +-1 or more occurrence,?-one or zero occurrence,{}-exact occurrence,|-either or,\d-digit,\D-not digit,\s-space,\S-without space
import re
x="the rain in spain"
y=re.search("^the.*spain$",x)
if y:
    print("matching")
else:
    print("not matching")

a=re.findall("ai",x)
print(a)

b=re.split("\s",x)
print(b)

c=re.sub("\s","#",x)
print(c)

import re
a=input("enter the password:")
flag=0
while True:
    if len(a)<8:
        flag=-1
        break
    elif not re.search("[a-z]",a):
        flag=-1
        break
    elif not re.search("[A-Z]",a):
        flag=-1
        break
    elif not re.search("[@_]",a):
        flag=-1
        break
    elif not re.search("[0-9]",a):
        flag=-1
        break
    elif re.search("/s",a):
        flag=-1
        break
    else:
        flag=0
        print("valid")
        break
if flag==-1:
    print("invalid")



