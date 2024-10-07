x=["guava","grapes","apple","orange","star fruit"]
print(len(x))
print(x)
print(type(x))
print(x[2])
print(x[3:5])
print(x[:5])
print(x[3:])
print(x[-1])
print(x[-4:-2])

for i in x:
    print(i)

x[1]="plums"
print(x)

x.append("kiwi")
print(x)
y=["red","green","blue","pink","yellow"]
print(y)
x.extend(y)
print(x)
x.insert(3,"star fruit")
print(x)
x.remove("plums")
print(x)
x.pop()
print(x)
x.pop(5)
print(x)
del x[3]
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
y.clear()
print(y)
a=x.copy()
print(a)
a=x+y
print(a)
x.clear()
print(x)
a.count("pink")
print(a)