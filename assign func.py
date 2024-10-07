#display only even no  from alist
l=[2,1,4,5,6,8]
a=list(filter(lambda x:x%2==0,l))
print(a)

#only odd nos
l=[2,1,4,5,6,8]
a=list(filter(lambda x:x%2!=0,l))
print(a)

#map squares of numbers
l=[2,1,4,5,6,8]
a=list(map(lambda x:x**2,l))
print(a)

#display squares of even numbers from a list
l=[2,1,4,5,6,8]
a=list(filter(lambda x:x%2==0,l))
print(a)
b=list(map(lambda x:x**2,a))
print(b)

#from a string list display length greater than 5
l1=["blue","black","red","majentha","indigo"]
c=list(filter(lambda d:len(d)>5,l1))
print(c)