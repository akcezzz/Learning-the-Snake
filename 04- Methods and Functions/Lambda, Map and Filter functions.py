###         Lambda expression, map and filter functions         ###

#the map function lets you apply a function to multiple elements

def square(n):
    return n**2

alist=[1,2,3,4,5]

for item in map(square,alist):
    print(item)

#other way

print(list(map(square,alist)))

#other example

def splicer(string):
    if len(string)%2 == 0:
        return 'EVEN'
    else:
        return string[0]


blist = ['Andy', 'Eve','Sally']
print(list(map(splicer,blist)))

def check_even(num):
    return num%2 == 0

#filter function example
#for booleans, will return only True's situations

clist = [1,2,3,4,5,6]

print(list(filter(check_even,clist))) ##will display only the results that return true

##Lambda's expression

#classical way of writing a function
def square2(num):
    return num**2

#lambda expression's way
lambda num: num**2

#or even
square = lambda x: x**2
print(square(2))

#using lambda expr. with map
print(list(map(lambda num: num**2, clist)))

#using lambda expr with filter function

print(list(filter(lambda num: num%2 == 0,clist)))