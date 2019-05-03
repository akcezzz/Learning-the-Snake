###         List Comprehension          ###

#COnsists of intializing lists in a fast way

mystring = 'Hello World'

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

#Or it is possible to initialize it directly into a variable declaration

alist = [letter for letter in mystring] #must put letter twice, once before for, and second time after

print(alist)

anotherlist = [x for x in range(1,11) if x%2==0]    #creates a list with even numbers, the if statement is inside the list and after the for loop

print(anotherlist)

#arithmetic could be used in declaring lists using the for loop

celsius = [0,23,54,45,19]

kelvins = [(temp+273) for temp in celsius]  #creating list converting celsius into fahrenheit
print(kelvins)


#using if and else statements into a list initialization

listb = [x if x%2 ==0 else 'ODD' for x in range(0,11)]

print(listb)

#using a nested loop to initialize a list

clist = [x*y for x in [2,4,6] for y in [1,10,100] ]

print(clist)