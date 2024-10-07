x="futura labs"
print(type(x))
for i in x:
    print(i)

l=[1,2,3,4,5]
print(type(l))
for i in l:
    print(i)

t=(1,2,3,4,5,6)

print(type(t))
for i in t:
    print(i)

s={"dear","friend"}
print(type(s))
for i in s:
    print(i)

d={"name":"anju","age":24}
print(type(d))
for i in d:
    print(i)

#for numbers use range
for i in range(10):
    print(i)



for i in range(1,11,2):
    print(i)


#conditional statements
for i in range(1,21,2):
    print(i)
    if i==3:
        break

#nested loops
l1=["a","b","c","d"]
l2=[1,2,3,4]
for i in l1:
    for j in l2:
        print(i,j)

#pass
for i in l1:
    pass