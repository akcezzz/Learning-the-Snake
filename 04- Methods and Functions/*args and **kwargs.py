###         *args and **kwargs          ###

#*args are used to pass as many arguments as you wish (non-dictionaries arguments)

def afunct(*args):
    return sum(args) * 0.05

print(afunct(1,2,3,4,5,6,7,8,9,10)) #function will display 5% of the sum of the arguments passed


def another_funct(**kwargs):
    print(kwargs)


another_funct(fruit = 'apple', veggie = 'tomato', drink = 'pepsi', dessert = 'cake')
    #displays all the kwargs passed

def myfunct(*args, **kwargs): #must follow the arguments type order (args first, kwargs second in this case)
    print('I would like {} {}'.format(args[0],kwargs['fruit'])) #must specify the key to go through a kwarg/dictionary

myfunct(1,2,3,fruit = 'apple', veggie = 'tomato', drink = 'pepsi')
