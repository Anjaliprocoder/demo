#problem 1
#a=open("add2.txt","x")
#b=open("add1.txt","x")
a=open("add2.txt","w")
a.write("good morning have a nice day")
a=open("add2.txt","r")
c=a.read()
b=open("add1.txt","w")
b.write(c)

#a=open("a1.txt","x")
#b=open("a2.txt","x")
#c=open("a3.txt","x")
a=open("a1.txt","w")
a.write("I am Anjali\n")
a=open("a1.txt","r")
z=a.read()
b=open("a2.txt","w")
b.write("I am from Thrissur")
b=open("a2.txt","r")
x=b.read()
c=open("a3.txt","a")
c.write(z)
c.write(x)


