list=[1,2,3,4,5,6,7]
print(list)
print(len(list))

print(8 in list)
print(2 in list)
print(8 not in list)
print(2 not in list)

for i in list:
    print(i)

print(list[2])
print(list[2:5])
print(list[2:])
print(list[:5])
print(list[-1])
print(list[-3:-1])

print(list.count(2))
list[2]=10
list.append(8)
print(list)
list.insert(3,9)
print(list)

list.pop(3)
print(list)

list.remove(5)
print(list)

list1=["good","girl"]
print(list1)

list1.append("dancer")
print(list1)
list1.clear()
print(list)

#del list1
print(list1)

list3=[1,5,2,0,6,3,8,2]
print(list3)

list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

list.extend(list3)
print(list)

a=[1,2,3,4,5]
print(a)
b=a.copy()
print(b)

z=list3+a
print(z)