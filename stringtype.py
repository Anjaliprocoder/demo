x="python is a.programming language"
print(len(x))
print(type(x))

print("is" in x)#membership operator to check whether a string is present or not
print("of" in x)

print("a" not in x)#membership operator to check whether a string is present or not
print("of" not in x)


for i in x:
    print(i)

#string is considered as an array

for i in x:
    print(i)
print(x[5])
print(x[3:5])
print(x[3:])
print(x[:5])


#negative indexing used for fetching last string

print(x[-1])
print(x[-3:-1])


#string modification methods
print(x.upper())
print(x.lower())

y=" good morning"
print(y)
print(y.strip()) #to remove white space in starting or ending

print(y.replace("good","hy"))

print(x.split("."))#slicing
print(x.count("p"))

print(x+y)

a="good idea{}"
b=12
#print(a+b)  error for this add braces is formatting

print(a.format(b))

x="my name is \"anjali\""
print(x)