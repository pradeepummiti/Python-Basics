# Program 1: Demonstrate nested function defintions (LEGB rule)
'''
name = "This is a global string"

def greet():
  name = "Pradeep"

  # As per LEGB rule, this is the "L" level, since the variable is not present, it goes to "E" level
  def hello():
    print(f"Hello "+name)

  hello()

greet()
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Demonstrate nested function defintions (LEGB rule)
'''
name = "This is a global string"

def greet():

  # As per LEGB rule, this is the "L" level, since the variable is not present, it goes to "E" level.
  # Since the variable is not present here, it goes to "G" level.
  def hello():
    print(f"Hello "+name)

  hello()

greet()
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Demonstrate nested function defintions (LEGB rule)
'''
name = "This is a global string"

def greet():

  # As per LEGB rule, this is the "L" level, since the variable is not present, it goes to "E" level.
  # Since the variable is not present here, it goes to "G" level.
  def hello():
    print(f"Hello "+name)

  hello()

greet()
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Demonstrate local and global variable assignment
'''
x = 50
def func(x):
  print(f"X is {x}")

  # Re-assign the value of X
  x = 150
  print(f"The new value of X after re-assignment is {x}")


func(x)
'''
#---------------------------------------------------------------------------------------------------------
