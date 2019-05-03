###         Dictionaries            ###


#The elements of a dicts have 2 components: 'key1':'value1:
#You can put lists or dictionaries inside a dictionary
my_dict = {'name': ['Sam','Rachid', 'Rex'], 'age':1, 'apple':2.99}

print(my_dict)

#To print a dictionary element, you refer to this 'key'
print(my_dict['name']) #Will display the list linked to 'name'

print(my_dict['name'][2]) #Will display subscript 2 of the list linked to 'name'

#The keys() method
print(my_dict.keys()) #will return the keys of a dictionary

#The values() method
print(my_dict.values()) #Will return the values of a dictionary

#The items() method
print(my_dict.items())  #Will return both the keys and values of a dictionary


