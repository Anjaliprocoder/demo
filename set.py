#any types of datas can be given
#unordered
#unindexed
#unchangeable but can add and remove items
#duplicate values are not allowed


s={5,"new",1,"friend",7,"beginning"}
print(len(s))
print(type(s))

for i in s:
    print(i)

print("girl" in s)
print("girl" not in s)
print("is" in s)
print("is" not in s)

s.add(8)
print(s)

s.remove(8)
print(s)

s1={4,3,1,8,6,0}
print(s1)
s.update(s1)#addind two sets
print(s1)
#to remove an absent element 
s1.discard(9)
print(s1)

s1.discard(8)
print(s1)

s1.pop()
print(s1)

s2=s.union(s1)
print(s2)

s3=s.intersection(s1)
print(s3)

s4=s.difference(s1)
print(s4)

s.clear()
print(s)

del s1
print(s1)
