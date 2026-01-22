# Program 1: Generate the square of every number in a list using map() function
'''
def square(num):
  return num ** 2

my_num = [1, 2, 3, 4, 5]

for item in map(square, my_num):
  print(f"{item}")

print(f"{list(map(square, my_num))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Display the string Even for even number of characters in the name, if not, return the 
# actual name using map() function
'''
def splicer(mystring):
  if (len(mystring) % 2 == 0):
    return "EVEN"
  else:
    return mystring

my_names = ["Andy", "Eve", "Sally"]

print(f"{list(map(splicer, my_names))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display the even numbers from a list of numbers using filter() function
'''
def check_even(num):
  return num % 2 == 0

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"{list(filter(check_even, my_nums))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Display the square of an input number
'''
def square_num(num):
  return num ** 2

print(f"The square of 3 is {square_num(3)}")
print(f"The square of 4 is {square_num(4)}")
print(f"The square of 5 is {square_num(5)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Display the square of an input number using lambda expression
'''
square_num = lambda num: num ** 2

print(f"The square of 3 is {square_num(3)}")
print(f"The square of 4 is {square_num(4)}")
print(f"The square of 5 is {square_num(5)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Display the square of input numbers using lambda expression and map() function
'''
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"{list(map(lambda num: num ** 2, my_nums))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Display the square of input numbers using lambda expression and filter() function
'''
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"{list(filter(lambda num: num % 2 == 0, my_nums))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Display the first characters of a list that contains names using map() and lambda expression
'''
my_names = ["Andy", "Eve", "Sally"]

print(f"{list(map(lambda name: name[0], my_names))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Display the characters of names in reverse using map() and lambda expression
'''
my_names = ["Andy", "Eve", "Sally"]

print(f"{list(map(lambda name: name[::-1], my_names))}")
'''
#---------------------------------------------------------------------------------------------------------
