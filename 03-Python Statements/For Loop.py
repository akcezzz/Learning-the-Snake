###         The for loop            ###

#Basic example

mylist = [1,2,3,4,5,6,7,8,9,10]

for i in mylist:        #Will loop the list automatically, no need to determine size, jump, etc. i (or any other variable
    #is declared as an element of the list
    print(i)

for _ in mylist:    #Best practice: use: '_' when you dont intend to use the content of a list but display someting list.len() times
    print('Hello')      #No need to print the content of a list, lists sizes can be used to print anything a certain number of time
    #This code will print hello 10 times


#Combining for loop and control statement

for i in mylist:
    if i % 2 == 0:      #Will print odd numbers of mylist
        print(i)
    else:
        print(f'Odd number: {i}') #Will print the odd numbers, string formatting is used here

#Getting the sum of every number on mylist

listSum = 0

for i in mylist:
    listSum += i
    if i==10:
        print(f'The sum is {listSum}')

#Looping a string#

mystring = 'Hello World'

for letter in mystring:
    print(letter)

### Looping a tuple ###

alist = [(1,2),(3,4),(5,6),(7,8)]

for item in alist:
    print(item)     #will display the tuples: (1,2), (3,4), etc.

#***Tuples unpacking
for (a,b) in alist:  #notation a,b without parenthesis works as well
    print(a)
    print(b)        #Will unpack the tuples, and display the whole content of the list

alist = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in alist:
    print(a,b,c)
    print(a)
    print(b)
    print(c)


#Looping a dictionary#

dict = {'k1':1,'k2':2,'k3':3}

for items in dict:
    print(items) #Displays only the keys by default

for items in dict.items():
    print(items)    #Will display the items of the dict

for key,value in dict.items():
    print(key, ' = ', value)        #prints both, can play with that the same way as tuples


#Appendice

#For loop notation:  for 'variable/object' in <iterable object>: