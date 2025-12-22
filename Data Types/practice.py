# Program 1: Write an equation using basic arithmetic operators to display the result as 100.25
'''
# Calculate the equation
result = 10 ** 2 * 2 /20 + 100 - 9.75

# Display the result
print(f"The value of result is: {result}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Display the results of below equations
'''
# Calculate equation 1
result1 = 4 * (6 + 5)

# Calculate the equation 2
result2 = 4 * 6 + 5

# Calculate the equation 3
result3 = 4 + 6 * 5

# Display the results
print(f"The value of result 1 is: {result1}")
print(f"The value of result 2 is: {result2}")
print(f"The value of result 3 is: {result3}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display the data type of the expression
'''
# Calculate equation
result1 = 3 + 1.5 + 4

# Display the data type of result
print(f"The data type of the expression 3 + 1.5 + 4 is: {type(result)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Determine the square root and square of a number
'''
# Calculate the square root
result_sqrt = 9 ** 0.5

# Display the square root of the number
print(f"The square root of 9 is: {result_sqrt}")

# Calculate the square
result_sq = 9 ** 2

# Display the square of the number
print(f"The square of 9 is: {result_sq}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Display a character from a string
'''
# Assign the string to a variable
my_string = "Hello"

# Display the character 'e' from the string
print(f"{my_string[1]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Reverse the string using slicing
'''
# Assign the string to a variable
my_string = "Hello"

# Display the string in reverse order
print(f"{my_string[::-1]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Display the last character of a string in two different ways
'''
# Assign the string to a variable
my_string = "Hello"

# Display the last character in the string using indexing
print(f"The last character from the string using indexing is: {my_string[4]}")

# Display the last character in the string using slicing
print(f"The last character from the string using indexing is: {my_string[-1]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Develop a list of 0,  0, 0, in two different ways
'''
# Build the list in first method
my_list1 = [0, 0, 0]

# Build the list in second method
my_list2 = [0]

# Display the list in first method
print(f"The first method is: {my_list1}")

# Display the list in second method
print(f"The second method is: {my_list2 * 3}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Replace an object in a list with a string
'''
# Assign the original list to a variable
my_list = [1, 2, [3, 4, 'Hello']]

# Display the original list
print(f"The original list: {my_list}")

# Replace 'Hello' with 'Goodbye' from the original list
my_list[2][2] = 'Goodbye' 

# Display the updated list
print(f"The updated list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Sort the numbers in a list
'''
# Assign the original list to a variable
my_list = [5, 3, 4, 6, 1]

# Display the original list
print(f"The original list: {my_list}")

# Sort the list
my_list.sort()

# Display the sorted list
print(f"The sorted list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Display 'hello' from the dictionary defined
'''
# Assign the dictionary to a variable
my_dict = {'simple_key': 'hello'}

# Display the original list
print(f"The word from the dictionary define is: {my_dict['simple_key']}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Display 'hello' from the dictionary defined
'''
# Assign the dictionary to a variable
my_dict = {'k1':{'k2':'hello'}}

# Display the original list
print(f"The word from the dictionary defined is: {my_dict['k1']['k2']}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Display 'hello' from the dictionary defined
'''
# Assign the dictionary to a variable
my_dict = {'k1':[{'nest_key':['this is deep', ['hello']]}]}

# Display the original list
print(f"The word from the dictionary defined is: {my_dict['k1'][0]['nest_key'][1][0]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Display 'hello' from the dictionary defined
'''
# Assign the dictionary to a variable
my_dict = {'k1':[1, 2, {'k2':['this is tricky', {'tough':[1, 2, ['hello']]}]}]}

# Display the original list
print(f"The word from the dictionary defined is: {my_dict['k1'][2]['k2'][1]['tough'][2][0]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 15: Display the unique values from the list
'''
# Assign the list to a variable
my_list = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]

# Display the original list
print(f"The original list is: {my_list}")

# Display the set with only the unique values from the list
print(f"The set is: {set(my_list)}")
'''
#---------------------------------------------------------------------------------------------------------
