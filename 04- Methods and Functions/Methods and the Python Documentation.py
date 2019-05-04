###         Methods and the Python Documentation            ###

#Functions are essentially the same as in C/C++

def hello_world():
    '''
    DOCSTRING: This is a place where you can document your function and explains how it is ued
    This functino is used to print hello world
    '''
    print('Hello World')

hello_world()

#function with a default parameter

def say_hello(name = 'Sammy'):
    '''
    DOCSTRING: This function has a default argument, prints the name sammy if nothing is passed to it
    '''
    print('Hello ' +name)

say_hello()