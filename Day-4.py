#List--->
mylist = [1,2,3]
mylist1 = [1.2,1.3,1.4]
mylist2 = ["a","b","c"]

print(mylist[2])
print(mylist[-1])

#Slicing--->
mylist3 = [1,2,3,4,5,6,7,8]
print(len(mylist))
print(mylist3[1:4])
print(mylist3[:4])
print(mylist3[1:])

mylist4 = [1,2,3,1.2,1.3,"abc","efg","a",True,False]
print(mylist4[-6:-3])
mylist4[1:3] = "change"
print(mylist4)
mylist4[1:4] = [0,9,8]
print(mylist4)

# Buit-in function---->
# insert()

mylist5 = [1,2,3]
mylist5.insert(2,"hello")
mylist5.append("hello")
print(mylist5)

# Extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)
a.remove(1)
a.pop()
a.clear()
# del a //delet entire list from the memory
print(a)

x = [1,2,3,4,5,6,7,8]
for i in range(len(x)):
    print(i)
    print(x[i])

for i in x:
    print(i)

x.sort()
x.reverse()
x.copy()
print(x.count(7))
print(x)

# Tupples--->
y = (1,2,2,3,4,"a","b",True)
z = [1,3,32]
print(type(y))
print(type(z))

print(y[:3])

tup = ("cat","dog","bird")
print(tup)
q = list(tup)
q.append("hourse")
print(q)

# SETS--->
e = {1,8,9,6,0}
print(len(e))

e.add(5)
e.remove(6)
e.discard(5) # never give error when the elements is not present in the set
e.update(y) # updaate the e set
e.intersection(y)
v = e.union(y) # update in the new set 
print(e)