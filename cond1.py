a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if a>b and a>c:
    print(a,"is greater")

elif b>c and b>a:
    print(b,"is greater")

else:
    print(c,"is greater")

#check whether a number is positive,neative or zero
x=int(input("enter num1:"))
if x>0:
    print(x,"is positive")
elif x<0:
    print(x,"is negative")
else:
    print(x,"is zero")

#check whether a number is odd or even
x=int(input("enter n:"))
if x%2==0:
    print("even")
else:
    print("odd")

#check  whether a year is leap year or not
a=int(input("enter year:"))
if a%4==0 and a%100!=0 or a%400==0:
    print("leap year")
else:
    print("not leap year")


#check whether a num is divisible by both 5 and 7
a=int(input("enter num:"))
if a%5==0 and a%7==0: 
    print(a,"is divisible") 
else:
    print("not divisible")  

