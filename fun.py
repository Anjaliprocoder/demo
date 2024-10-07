#functions are block of code helps in code reuseability by calling
#parameters are datas passing to a func while defining it.
#arguments are informn passing.(when call then it executes)
#def is keyword used to define function in python

def sample():
    print("this is my first function")
sample()

def add(a,b):
    c=a+b
    print(c)
add(1,2)

#arbitrary arguments-represented by-"*args"-when how many arguments are passed is unknown
def first(*x):
    print(x[2]+x[1])
first(1,2,3,9,6)

#keyword arguments-arguments are passed in the form of key=value,represented by "kwargs"
def first(x,y):
    print(x+y)
first(y=3,x=10)

#arbitrary keyword arguments-how many keyword arguments are passing is unknown,represented by **kwargs
def first(**x):
    print(x["name"])
first(name="anjali")

def default(x=4):
    print(x)
default()
def default(x=4):
    print(x)
default(12)

#return statement
def fun(x,y):
    z=x+y
    return(z)
print(fun(6,2))

#pass-now no datas are not given but want to give in future so to remove error
def fun():
    pass

l1=["blue","red","black"]
def colour(l1):
    for i in l1:
        print(i)
colour(l1)

#lamda-a func-any no of arguments can be given but one expression,for a short period of time
lambda args:expression,map and filter are func used with this
a=lambda x,y:x+y
print(a(2,3))

l=["orange","apple","grapes"]
x=list(map(lambda y:y.upper(),l))
print(x)

l1=[1,6,3,2,5]
x=list(filter(lambda y:y>2,l1))
print(x)

    

 

