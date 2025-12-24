# Program 1: Iterate through numbers 1 to 10 using a for-loop
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
  print(f"{num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Display the string "Hello" 10 times using a list and a for-loop
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
  print(f"Hello")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display the even numbers from a list of numbers between 1 to 10 using a for-loop
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
  # Check for even numbers from the list
  if ((num % 2) == 0):
    print(f"{num} is an even number")
  else:
    print(f"{num} is an odd number")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Calculate the sum of numbers in a list of numbers between 1 to 10 using a for-loop
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sum = 0

for sum in my_list:
  # Perform the addition
  my_sum = my_sum + sum
  
print(f"The total sum is: {my_sum}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Calculate the sum of consecutive numbers (running tally) between 1 to 10 using a for-loop
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sum = 0

for sum in my_list:
  # Perform the addition
  my_sum = my_sum + sum
  print(f"The sum is: {my_sum}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Display individual letters in a string using a for-loop
'''
my_string = "Hello World"

for letter in my_string:
  print(f"{letter}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Display individual letters in a string using a for-loop
'''
for _ in "Hello World":
  print(f"{_}")

for _ in "Hello World":
  print(f"{"cool}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Iterate through numbers 1 to 10 using a for-loop
'''
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in my_tuple:
  print(f"{num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Unpack the elements of a tuple pair from the list using a for-loop
'''
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for item in my_list:
  print(f"{item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Display individual elements from each tuple pair in a list using for-loop
'''
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
  print(f"{a}")
  print(f"{b}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Display only the first elements from each tuple pair in a list using for-loop
'''
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
  print(f"{a}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Display only the second elements from each tuple pair in a list using for-loop
'''
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
  print(f"{b}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Display only the second elements from each tuple pair in a dictionary using for-loop
'''
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
  print(f"{b}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Display only the key in a dictionary using for-loop
'''
my_dict = {"k1": 1, "k2":2, "k3":3}

for item in my_dict:
  print(f"{item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 15: Display the key-value pairs in a dictionary using for-loop
'''
my_dict = {"k1": 1, "k2":2, "k3":3}

for pairing in my_dict.items():
  print(f"{pairing}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 16: Display the key-value pairs individually from a dictionary using for-loop
'''
my_dict = {"k1": 1, "k2":2, "k3":3}

for (key, value) in my_dict.items():
  print(f"Key: {key}")
  print(f"Value: {value}")

'''
#---------------------------------------------------------------------------------------------------------
# Program 17: Display only the values in a dictionary using for-loop
'''
my_dict = {"k1": 1, "k2":2, "k3":3}

for item in my_dict.values():
  print(f"{item}")
'''
#---------------------------------------------------------------------------------------------------------
