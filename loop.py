#to check truthness of a condition

i=1
while i<=10:
    print (i)
    i+=1

#display only odd and only even numbers

a=int(input("enter num:"))#odd
i=1
while i<=a:
    print(i)
    i+=2

a=int(input("enter num:"))#even
i=1
while i<=a:
    if i%2==0:
        print(i)
    i+=1

"""loop control statements are break,continue.
break is used to exit from a loop
continue is used to skip an StopIteration"""

i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1

i=0
while i<=10:
    i+=1
    if i==6:
        continue
    print(i)


