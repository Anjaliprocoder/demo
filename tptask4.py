t=(4,"hy","good",3,1,5)
print(len(t))
print(type(t))

print("hy" in t)
print("hy" not in t)

for i in t:
    print(i)

print(t[5])
print(t[1:5])
print(t[1:])
print(t[:5])
print(t[-3])
print(t[-3:-1])
print(t[-3:])
print(t[:-1])

l=list(t)
print(l)

l.append("everone")
print(l)

l.insert(2,"hoi")
print(l)

t1=(4,3,2,9)
t2=t+t1
print(t2)

a=2*t1
print(a)