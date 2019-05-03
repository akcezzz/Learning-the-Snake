###         Tuples          ###

#Tuples are like list, but they are immutable (their content cannot be changed)

t = (1, 'Lion', 2.33)   #Tuples can contain different data types
#t[0] = 3 is an error

x = ('a','b','c','a','a','A','b')

#The count() method

print(x.count('a')) #counts how many a's are here
print(x.count('A'))

#The index() method

print(x.index('A'))

#It is possible to declare nested lists inside tuples

a = (1,2,3,[4,5])