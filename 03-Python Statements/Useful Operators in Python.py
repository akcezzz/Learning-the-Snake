###         Useful Operators            ###

#For loop's options

#It is possible to choose the range of a for loop

alist = [1,2,3,4,5,6,7,8,9,10]

for i in range(10): # same as i<10. Will display 1-9, 10 is not included
    print(i)

for i in range(0,11,2): #format: start,end,jump
    print(i)


#Enumerate() function, lets you get the index of the for loop

astring = 'Sammy'

for items in enumerate(astring): #Displays each letter with its position in the for loop (tuples format)
    print(items)    #Ex: (0,'S')

#The zip() function. Lets you loop multiples lists, items at a time and displays them together

list1= [1,2,3,4,5]
list2= ['a','b','c','d','e']
list3 = [100,200,300,400,500]

for items in zip(list1,list2,list3): #The lists must have the same length for it to work, else its going to display until the biggest index in common
    print(items)

### Importing functions from libraries

from random import shuffle  #Shuffle is a function that scrambles a list

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)

print(mylist)

from random import randint #randint lets you grab a random integer

a = randint(0,100) #format (lower range, upper range)

print(a)

###Getting input from the user

result = input("Please, enter a number: ") #The result will be saved as a string

result = int(result) #putting it back to an integer for example
print(result)




