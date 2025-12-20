# Program 1: Display the value of any key defined in a dictionary
'''
my_dict = {'key1':'value1', 'key2':'value2'}

# Display the value of the keys
print(f"The value of 'key1' is: {my_dict['key1']}")
print(f"The value of 'key2' is: {my_dict['key2']}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Include a list and a dictionary as values to keys inside a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': [0, 1, 2, 3], 'key4': {'k1':'inside', 'k2': 44, 'k3': 'outside'}}

# Display the value of the keys
print(f"The original dictionary is: {my_dict}")
print(f"The value of list is: {my_dict['key3']}")
print(f"The value of dictionary is: {my_dict['key4']}")
print(f"The value of key 2 inside the nested dictionary is: {my_dict['key4']['k2']}")
print(f"The value of index 2 inside the nested list is: {my_dict['key3'][2]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Change the value of a list inside a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': [0, 1, 2, 3], 'key4': {'k1':'inside', 'k2': 44, 'k3': 'outside'}}

print(f"The original dictionary is: {my_dict}")
my_list = my_dict['key3']
print(f"The value of list is: {my_list}")
my_list[2] = 'TWO'
print(f"The value of modified list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Add a new 'key':'value' pair to an existing dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': 99}

print(f"The original dictionary is: {my_dict}")
my_dict['key4'] = 'Hello'
print(f"The updated dictionary is: {my_dict}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Override an existing 'key':'value' pair in a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': 99}

print(f"The original dictionary is: {my_dict}")
my_dict['key2'] = 35
print(f"The updated dictionary is: {my_dict}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Display only the keys in a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': 99}

print(f"The original dictionary is: {my_dict}")
print(f"The keys in the dictionary are: {my_dict.keys()}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Display only the values in a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': 99}

print(f"The original dictionary is: {my_dict}")
print(f"The values in the dictionary are: {my_dict.values()}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Display respective pairings in a dictionary
'''
my_dict = {'key1': 123, 'key2':'55.77', 'key3': 99}

print(f"The original dictionary is: {my_dict}")
print(f"The items in the dictionary are: {my_dict.items()}")
'''
#---------------------------------------------------------------------------------------------------------
