# Program 1: Calculate the 5% of the sum of 2 input numbers
'''
def sum_func(a, b):
  my_sum = a + b

  return 5/100 * my_sum

res = sum_func(10, 20)
print(f"5% of the sum of 10, 20 is {res}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Calculate the 5% of the sum of any number of inputs to a function
'''
def sum_func(*args):
  return sum(args) * 0.05

res = sum_func(10, 20, 10, 40, 50)
print(f"5% of the sum is is {res}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display the contents of a loop using *args concept
'''
def my_func(*args):
  for item in args:
    print(f"{item}")

my_func(10, 20, 10, 40, 50)
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Display the contents using **kwargs concept
'''
def my_func(**kwargs):
  print(f"{kwargs}")
  if 'fruit' in kwargs:
    print(f"My fruit of choice is {kwargs['fruit']}")
  else:
    print(f"No fruit found")

my_func(fruit = "apple", veggie = "potato")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Display the contents using *args and **kwargs concept
'''
def my_func(*args, **kwargs):
  print(f"I would like to have {args[0]} {kwargs["food"]}")

my_func(10, 20, 30, 40, fruit = "apple", food = "potato")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Display a list containing only those arguments that are even contents 
'''
def myfunc(*args):
    even_list = []
    for num in args:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

myfunc(5,6,7,8)
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Display a string where every even letter is uppercase, and every odd letter is lowercase.
'''
def myfunc(str_word):
    string = []
    index = 0
    for letter in str_word:
        if index % 2 == 0:
            string.append(letter.upper())
            index = index + 1
        else:
            string.append(letter.lower())
            index = index + 1
    return "".join(string)

myfunc('Anthropomorphism')
'''
#---------------------------------------------------------------------------------------------------------
