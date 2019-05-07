###         Sets            ###


#Declaring a set

myset = set({1,2})

#Sets elements are unique (cannot occur twice)

myset.add(3)
print(myset)
#myset.add(3) will do nothing

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]

myset = set(mylist)
print(myset) #prints 1,2,3,4 only
