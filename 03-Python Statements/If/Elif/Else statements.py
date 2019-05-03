###         If/Elif/Else            ###

#If/else statement

number1 = 5
number2 = 4

if number1>number2:     #uses a colon after the condition
    print(number1, " is greater than ", number2)
else:       #colon after the else, else have to be to same indent level to the if to be linked to it
    print(number2, " is greater than ", number1)

hungry = True

if hungry:
    print('FEED!')
    hungry = False      #A if/else condition is linked to the initial condition only, reinitializing a variable inside an if wont affect the else statement
else:
    print('REST!')

##The elif statement (same as an else if() in C/C++

age = 19

if age < 18:
    print('You are underage')
elif age>=18 and age<=30:
    print('You are a young adult')
else:
    print('You are an adult')

