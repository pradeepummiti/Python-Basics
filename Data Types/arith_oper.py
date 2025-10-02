# Program 1: Addition of two numbers with inputs already provider
'''
num1 = 10
num2 = 25

# Add the numbers
sum_result = num1 + num2

# Display the sum
print(f"The sum is: {sum_result}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Addition of two numbers by getting inputs from the user
'''
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert the input strings to numbers (integers or floats)
# Use int() for whole numbers, float() for decimal numbers
num1 = float(num1_str) 
num2 = float(num2_str)

# Add the numbers
sum_result = num1 + num2

# Display the sum
print(f"The sum of {num1} and {num2} is: {sum_result}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Subtraction of two numbers with inputs already provider
'''
num1 = 25
num2 = 10

# Subtract the numbers
diff_result = num1 - num2

# Display the difference
print(f"The sum is: {diff_result}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Subtraction of two numbers by getting inputs from the user
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
difference = num1 - num2
print(f"The difference is: {difference}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Subtraction of two numbers by defining a subtraction function for re-useability
'''
def subtract_numbers(a, b):
  return a - b

result = subtract_numbers(20, 7)
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Subtraction of two numbers by using a operator.sub() function
'''
import operator

num1 = 15
num2 = 8
difference = operator.sub(num1, num2)
print(difference)
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Multiplication of two numbers with inputs already provider
'''
num1 = 10
num2 = 3
product = num1 * num2
print(product)
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Multiplication of two numbers with inputs already provider
'''
result = 5 * 7
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Multiplication of two numbers by defining a Multiplication function for re-useability
'''
def multiply_numbers(a, b):
  return a * b

result = multiply_numbers(8, 4)
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Multiplication of two numbers by getting inputs from the user
'''
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert the input strings to numbers (integers or floats)
# Use int() for whole numbers, float() for decimal numbers
num1 = float(num1_str) 
num2 = float(num2_str)

product = num1 * num2
print(f"The product of {num1} and {num2} is: {product}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Divison of two numbers with a true division (floating-point) result
'''
num1 = 10
num2 = 3
result = num1 / num2
print(result)  # Output: 3.3333333333333335
'''
'''
num3 = 8
num4 = 2
result2 = num3 / num4
print(result2) # Output: 4.0
'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Divison of two numbers with a floor division (integer) result
'''
num1 = 10
num2 = 3
result = num1 // num2
print(result)  # Output: 3
'''
'''
num3 = 8
num4 = 2
result2 = num3 // num4
print(result2) # Output: 4
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Divison of two numbers to handle division-by-zero error
'''
dividend = 10
divisor = 0

try:
    result = dividend / divisor
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Basic modulo operation
'''
result_int = 10 % 3
print(f"10 % 3 = {result_int}")  # Output: 1
'''
#---------------------------------------------------------------------------------------------------------
# Program 15: Modulo operation with atleast one negative input number
'''
result_neg_divisor = 7 % -3
print(f"7 % -3 = {result_neg_divisor}")  # Output: -2 (remainder takes sign of divisor)
'''

'''
result_neg_dividend = -7 % 3
print(f"-7 % 3 = {result_neg_dividend}")  # Output: 2 (remainder takes sign of divisor)
'''
#---------------------------------------------------------------------------------------------------------
# Program 16: Modulo operation with floating-point inputs (can have precision issues)
'''
result_float = 10.5 % 2.2
print(f"10.5 % 2.2 = {result_float}") # Output: 1.6999999999999993
'''
#---------------------------------------------------------------------------------------------------------
# Program 17: Modulo operation to check for even/odd numbers (can have precision issues)
'''
def check_parity(number):
    if number % 2 == 0:
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"

print(check_parity(4))  # Output: 4 is an even number
print(check_parity(7))  # Output: 7 is an odd number
'''
#---------------------------------------------------------------------------------------------------------
# Program 18: Modulo operation on exponentiation (x^y) % p using python's built-in pow() function
'''
x = 2
y = 5
p = 13
result_mod_exp = pow(x, y, p)
print(f"({x}^{y}) % {p} = {result_mod_exp}")  # Output: 6
'''
#---------------------------------------------------------------------------------------------------------
# Program 19: Power of a number, in this case, to calculate 4 to the power of 3 (4 * 4 * 4)
'''
result = 4 ** 3
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 20: Power of a number, in this case, to calculate 3 to the power of 4 using pow() function
'''
result = pow(3, 4)
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 21: Power of a number using math.pow() function
'''
import math

result = math.pow(5, 2)
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 22: Order of operations involving addition, subtration, multiplication, division, exponentiation
'''
result = 2 + 3 * 4 - (6 / 2) ** 2
print(result)
'''
#---------------------------------------------------------------------------------------------------------
# Program 23: Single expression to print 100 using more than one arithmetic operaors
'''
result = 150 - 50 - 10 + 10
print(f"The sum is: {result}")
'''
#---------------------------------------------------------------------------------------------------------
