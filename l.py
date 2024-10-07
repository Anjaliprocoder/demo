#identity operators is,is not when same objects are present
#(),exponents,mult,div,modulus,add,sub,bitwise,comp,logical-precedence order
"""list features
items are ordered-indexed
changeable or mutable
duplicate values are allowed"""

list=[1,2,3,4,5]#access items
print(list)
print(len(list))
print("a" in list)

print(1 in list)
print(list[2])
print(list[1:3])
print(list[1:])
print(list[:3])
print(list[-3:-1])

for i in list:
    print(i)

list[2]=10
print(list)

list.append(5)#method to add at end
print(list)

list.insert(2,7)#add at particular position
print(list)

list1=["hello","good","morning"]
list.extend(list1)
print(list)

list1.remove("good")
print(list1)

list1.pop(1)
print(list1)

list.pop()
print(list)

del list[2]
print(list)

list2=["hy","anjali"]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

z=list2.copy()
print(z)

z=list1+list2
print(z)

list1.clear()
print(list1)
 
del list1
#print(list1)

list2.count(2)
print(list2)
