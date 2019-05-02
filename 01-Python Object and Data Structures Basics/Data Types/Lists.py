####        LISTS           ####

my_list = ['Hello', 1, 2.33]
alist = ['z','p','a','m','h','l'] #unsorted list of characters
blist = [34,23,1,7,87,45,422] #unsorted list of integers

print(my_list)  #Lists can be printed as they are
print(my_list[2]) #lists can be printed using indexes

my_list[0] = 'Python'
print(my_list) #Lists can be modified

#The append() method

my_list.append('apple') #Lets you add an element at the end of the list
print(my_list)

#The pop() method

my_list.pop() #Lets you remove an element at the end of the list by default
my_list.pop(1) #or by precising a subscript
print(my_list)

#The sort() method
#Lets you sort a list in alphabetical order/smaller-to-greater but DOESNT RETURN ANYTHING

alist.sort()
blist.sort()
print(alist + blist)

#Lists can be added using operators
clist = alist + blist
print(clist)