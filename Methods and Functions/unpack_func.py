# Program 1: Demonstrate tuple unpacking without using the concept of functions
'''
my_tuple = [("CMPY1", 1), ("CMPY2", 2), ("CMPY3", 3)]

for item in my_tuple:
  print(f"{item}")

for stk_name, stk_price in my_tuple:
  print(f"{stk_name}")
  print(f"{stk_price}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Demonstrate tuple unpacking using the concept of functions
'''
my_tuple = [("EMP1", 1), ("EMP2", 3), ("EMP3", 2)]

def emp_hours_check(my_tuple):
  emp_name = ""
  work_hours = 0

  for emp, hours in my_tuple:
    if (hours > work_hours):
      work_hours = hours
      emp_name = emp
    else:
      pass

  return (emp_name, work_hours)

return_value = emp_hours_check(my_tuple)

print(f"{return_value}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Randomly shuffle the contents in a list
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from random import shuffle
shuffle(my_list)

print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Randomly shuffle the contents in a list by defining a new function
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def shuffle_list(mylist):
  shuffle(mylist)

  return (mylist)

return_value = shuffle_list(my_list)

print(f"{return_value}")
'''
#---------------------------------------------------------------------------------------------------------
