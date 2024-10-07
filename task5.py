#find sum of first n natural numbers
a=int(input("enter num:"))
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)

#sum of even numbers in a range
a=int(input("enter num:"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)

#find the factorial of number
a=int(input("enter num:"))
n=1
for i in range(1,a+1):
       n=n*i
print(n)

#find sum of square of first n natural numbers
a=int(input("enter num:"))
sum=0
for i in range(1,a+1):
       sum=sum+(i*i)
print(sum)

#check whether a number is prime or not
a=int(input("enter num:"))
n=0
for i in range(1,a+1):
    if a%i==0:
        n+=1
if n==2:
    print("prime")
else:
    print("not prime")

#generate fibonacci sequence upto a specified number
a=int(input("enter num:"))
j=1
for i in range(1,a+1):
    j=i+(i-1)
    print(j)



