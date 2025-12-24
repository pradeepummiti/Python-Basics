# Program 1: Display all integers below 10 using range function
'''
for num in range(10):
  print(f"{num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Display all integers between 3 and 10 using range function
'''
for num in range(3, 10):
  print(f"{num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display all integers below 15 in steps of 2 using range function
'''
for num in range(0, 15, 2):
  print(f"{num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Display all integers below 15 in steps of 2 using range function and not a for loop
'''
print(f"{list(range(0, 15, 2))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Display individual characters along with its position in the word using enumerate function
'''
my_word = "Hello"

for item in enumerate(my_word):
  print(f"{item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Demonstrate zip function by zipping two different lists
'''
my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = ["a", "b", "c", "d", "e"]

for item in zip(my_list1, my_list2):
  print(f"{item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Generate a list of tuples using the  zip function
'''
my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = ["a", "b", "c", "d", "e"]
my_list3 = [100, 200, 300]

print(f"{list(zip(my_list1, my_list2, my_list3))}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Check if a letter is present in a list using the in keyword
'''
print(f"{"x" in ["x", "y", "z"]}")
print(f"{"x" in [1, 2, 3, 4]}")

'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Check if a letter is present in a string using the in keyword
'''
print(f"{"x" in "x-mas"}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Check if a key is present in a dictionary using the in keyword
'''
my_dict = {"k1": 1, "k2": 2, "k3":3}

print(f"{"k4" in my_dict}")
print(f"{"k1" in my_dict.keys()}")
print(f"{"5" in my_dict.values()}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Display maximum and minimum numbers in a list of numbers
'''
my_list = [100, 20, 30, 40, 50, 60]

print(f"Minimum number from the list: {min(my_list)}")
print(f"Maximum number from the list: {max(my_list)}")

'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Shuffle the contents of list using the shuffle function
'''
from random import shuffle

my_list = [100, 20, 30, 40, 50, 60]

shuffle(my_list)

print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Generate an integer randomly between 0 and 100 using the randint function
'''
from random import randint

print(f"{randint(0, 100)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Allow the user to enter the input using input function
'''
num = input("Enter the number: ")
print(f"The number entered by the user is: {num}")
print(f"The type of variable num is: {type(num)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 15: Allow the user to enter the input using input function
'''
num = float(input("Enter the number: "))
print(f"The number entered by the user is: {num}")
print(f"The type of variable num is: {type(num)}")
'''
#---------------------------------------------------------------------------------------------------------
