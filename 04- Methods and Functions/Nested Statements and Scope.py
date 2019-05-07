###         Nested Statements and Scope         ###

# 4 types of variables

    #Local: assigned in a function
    #Enclosing function local: assigned in the local scope of a function
    #Global variable: assigned at the top level of module file
    #Build-in: names pre-assigned in the built-in names modules

#local:

lambda num: num**2  #Num is local to the lambda function

#passing something by reference using the global statement

x = 35

def x10times():
    global x #global here to reach x = 35
    x=x*10 #global x is getting changed


x10times() #function call that multiply x by 10

print(x) #x = 350