# Program 1: Create a list of individual letters from the string using a for-loop
'''
my_string = "Hello"
my_list = []

for letters in my_string:
  my_list.append(letters)
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Create a list of individual letters from the string using list comprehension
'''
my_string = "Hello World"
my_list = [letters for letters in my_string]
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Create a list of numbers from 0 to 10 using list comprehension
'''
my_list = [num for num in range (0, 11)]
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Display the square of numbers from 0 to 10 using list comprehension
'''
my_list = [num ** 2 for num in range (0, 11)]
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Check for even numbers between 0 to 10 using list comprehension
'''
my_list = [num for num in range (0, 11) if (num % 2 == 0)]
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Convert tempearature values from Celcius to Fahrenheit using list comprehension
'''
celsius_list = [10, 40, 80]

fahrenheit_list = [(((9/5) * temp) + 32) for temp in celsius_list]
print(f"{fahrenheit_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Demsontrate nested for-loops using list comprehension
'''
my_list_normal = []

for x in [2, 4, 6]:
  for y in [1, 3, 5]:
    my_list_normal.append(x * y)

print(f"my_list_normal = {my_list_normal}")

my_list_comprh = [a * b for a in [2, 4, 6] for b in [1, 3, 5]]
print(f"my_list_comprh = {my_list_comprh}")
'''
#---------------------------------------------------------------------------------------------------------
