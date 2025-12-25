# Program 1: Print out only words that start with the letter "s" using "if" and ".split()"
'''
st = "Print only the words that start with s in this sentence"
my_list = []

for letter in st.split():
    if (letter[0] == "s"):
      my_list.append(letter)
print(f"Found a word starting with 's': {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Use range() function to print all even numbers from 0 to 10
'''
my_list = []

for num in range(0, 11):
    if (num % 2 == 0):
      my_list.append(num)

# Display the result
print(f"The new list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Use list comprehension technique to display a list of numbers from 1 to 50 that divisible by 3
'''
my_list = [num for num in range (1, 51) if ((num % 3) == 0)]

# Display the result
print(f"The new list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Iterate through a string and if the length of words is even, display "EVEN"
'''
st = "Print every word in this sentence that has an even number of letters"

for letter in st.split():
  if ((len(letter) % 2) == 0):
    print(f"{letter}: EVEN")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Display integers from 1 to 100. For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number. For multiples of 3 and 5, print "FizzBuzz".
'''
my_list = []

for num in range(1, 101):
  if (((num % 3) == 0) and ((num % 5) == 0)) :
    my_list.append("FizzBuzz")
  elif ((num % 3) == 0):
    my_list.append("Fizz")
  elif ((num % 5) == 0):
    my_list.append("Buzz")    
  else:
    my_list.append(num)

# Display the result
print(f"{my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Use list comprehension technique to create a list of first letters of every word from a string
'''
st = "Create a list of the first letters of every word in this string"

my_list = [letter[0] for letter in st.split()]

# Display the result
print(f"The new list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
