#This file contains examples of strings usage

#Declaring a string:

#Strings can be declared using single-quotes or double-quotes
my_string = 'Hello'
my_string2 = "World"

#The len() function lets you verify the length of a string (spaces are counted)
print(len(my_string))
print(len(my_string+my_string2)) #Strings can be added to each other while using the function

#Strings can be used with operators
my_string3 = my_string + my_string2
print(my_string3)



##Indexing a string of characters

aString = 'abcdefg'

print(aString[2])   #Specific subscript
print(aString[-1])  #Reverse indexing (-1 = last subscript)
print(aString[2:])  #From 2 to the last subscript
print(aString[:5])  #From first subscript to 5 not included (5-1)
print(aString[0:3]) #From a to b (b is not included), in this case from subscript 0 to 2
print(aString[::])  #Displays the whole string (same as just printing the string itself

##Slicing a string
#Uses the notation [start:stop:step] where as step is the "jump". Same format as a for loop
print("\n\n")

string1 = 'axilation'

print(string1[::2]) #Starts from beginning to end, misses 1 letter on 2
print(string1[2:-1:2]) #Beginning until the end, misses 1 letter on 2 (The last subscript is not included if it is specified)

###REVERSING A STRING
print(string1[::-1]) #Here we are taking a reverse step, will display "noitalixa"