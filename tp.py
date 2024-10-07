#different datas can be given
#ordered
#immutable means unchangeable
#duplicate values are allowed,()

t1=(3,2,5,4,7,3)
print(len(t1))
print(type(t1))

print(1 in t1)
print(3 not in t1)
print(1 not in t1)
print(3 in t1)

print(t1[2])
print(t1[2:5])
print(t1[2:])
print(t1[:5])
print(t1[-4])
print(t1[-4:-1])
print(t1[-4:])
print(t1[:-1])

a=list(t1)
a.insert(2,5)
print(a)

a.append(10)
print(a)

a.remove(7)
print(a)

t1=tuple(a)
print(t1)

t2=("hello","everyone")
t3=t1+t2
print(t3)

z=t2*3
print(z.count("hello"))