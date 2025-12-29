# Program 1: Display "hello", "how", "are" and "you" using a function
'''
# Function definition
def say_hello():
  print(f"hello")
  print(f"how")
  print(f"are")
  print(f"you")

# Function call
say_hello()
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Display "Hello" and pass on the name as a function argument
'''
# Function definition
def say_hello(name):
  print(f"Hello {name}")

# Function call
say_hello("Pradeep")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Return the sum of two numbers from a function and display the output
'''
# Function definition
def sum_num(num1, num2):
  sum = num1 + num2  
  return sum

# Function call
result = sum_num(1, 2)
print(f"The sum of the numbers is {result}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Concatenate the input arguments by passing them into a function
'''
# Function definition
def sum_num(num1, num2):
  sum = num1 + num2  
  return sum

# Function call
result_num = sum_num(1, 2)
print(f"The sum of the numbers is {result_num}")

result_concate = sum_num("1", "2")
print(f"The result of the string input arguments is {result_concate}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Verify if an input argument number to a function is even
'''
# Function definition
def even_num(num):
  result = (num % 2) == 0
  return result

# Function call
result_num = even_num(10)
print(f"{result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Return true if any number in a list is even 
'''
# Function definition
def even_num_list(num_list):
  for num in num_list:
    if (num % 2 == 0):
      return True
    else:
      pass

# Function call

result_num = even_num_list([1, 3, 5, 7, 10])
print(f"{result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Return true if any number in a list is even, return False if it encounters an odd number
'''
# Function definition
def even_num_list(num_list):
  for num in num_list:
    if (num % 2 == 0):
      return True
    else:
      pass
  return False

# Function call

result_num = even_num_list([1, 3, 5, 7, 10])
print(f"{result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8 Return the even numbers from the list, return an empty list if there are all odd numbers
'''
# Function definition
def even_num_list(num_list):
  num_list_even = []
  for num in num_list:
    if (num % 2 == 0):
      num_list_even.append(num)
    else:
      pass
  return num_list_even

# Function call
result_num = even_num_list([1, 3, 5, 7, 10])
print(f"{result_num}")
'''
#---------------------------------------------------------------------------------------------------------
