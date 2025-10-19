# Program 1: Assigning a string within single quotes to a variable 
'''
name = 'Alice'

print(f"The name is: {name}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Assigning a string within double quotes to a variable 
'''
name = "Alice"

print(f"The name is: {name}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Assigning a sentence within double quotes to a variable 
'''
str = "I'm learning Python"

print(f"{str}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Assigning a sentence with a contraction (I'm) within single quotes to a variable (invalid)
'''
str = 'I'm learning Python'

print(f"{str}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Print two strings in different lines using two 'print' statements
'''
print("Hello World One")
print("Hello World Two")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Print a string in different lines with a single 'print' statement using newline functionality
'''
print("Hello \n World")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Print a string in single line with one 'print' statement using 'tab' functionality
'''
print("Hello \t World")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Determine the length of a string using 'len()' function
'''
str = "I'm learning Python"

print(f"The length of the string is: {len(str)} characters")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Display the first character in a string
'''
str = "I'm learning Python"

print(f"The first character in the string is: {str[0]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Display the second from last character in a string
'''
str = "I'm learning Python"

print(f"The first character in the string is: {str[-2]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Slice a string from second character till the last character
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[2:]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Slice a string upto third character in the string
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[:3]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Display 'def' in the below string
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[3:6]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Display the string from the beginning to the end with default step-size of 1
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[::]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 15: Display the string from the beginning to the end with step-size of 2
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[::2]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 16: Display a slice of the string with start, stop and step size
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[3:6:2]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 17: Reverse a string using step-size
'''
str = "abcdefghijkl"

print(f"The sliced string is character in the string is: {str[::-1]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 18: Change a string "Sam" to "Pam" using concatenation of strings
'''
name = "Sam"
name_slice = name[1:]
new_name = "P" + name_slice

print(f"The name {name} has been modified to {new_name}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 19: Change a string "Sam" by adding new contents using string concatenation
'''
str = "Hello World"
add_str = ". It's a beautiful world outside !"
new_str = str + add_str

print(f"The new string is displayed below\n{new_str}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 20: Display a single character several times using string multiplication
'''
str = "z"
new_str = str * 10

print(f"The new string is displayed below\n{new_str}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 21: Display a single character several times using string multiplication
'''
str = "damn"
new_str = str[3] * 10

print(f"The new string is displayed below\n{str + new_str}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 22: Make all characters in a string to be displayed in uppercase or lowercase
'''
str = "Hello World"

print(f"The new string in all uppercase is {str.upper()}")
print(f"The new string in all lowercase is {str.lower()}")

'''
#---------------------------------------------------------------------------------------------------------
# Program 23: Split the characters in a string based on whitespaces
'''
str = "Hello World"
add_str = ". It's a beautiful world outside !"
new_str = str + add_str

print(f"The split version of the new string is displayed below\n{new_str.split()}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 24: Split the characters in a string based on letter 'i'
'''
str = "Hi, this is a string !"

print(f"The split version of the new string is displayed below\n{str.split("i")}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 25: Insert a new character to an existing string using format() method
'''
str = "Hi, this is a string {}"

print(f"The new version of the string is dsipalyed below\n{str.format(" !")}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 26: Insert multiple characters to an existing string using format() method
'''
str = "The {} {} {}."

print(f"The new version of the string is dsipalyed below\n{str.format("fox", "brown", "quick")}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 27: Insert mulitple characters to an exsiting string using indices of format () method
'''
str = "The {2} {1} {0}."

print(f"The new version of the string is dsipalyed below\n{str.format("fox", "brown", "quick")}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 28: Insert mulitple characters to an exsiting string using keywords of format () method
'''
str = "The {q} {b} {f}."

print(f"The new version of the string is dsipalyed below\n{str.format(f = "fox", b = "brown", q = "quick")}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 29: Compute a floating-point precision to 3 decimal places using the format () method
'''
result = 100/7000

print("The new floating-point value of 100/7000 with 3 decimal places is {r:1.3f}".format(r = result))
'''
#---------------------------------------------------------------------------------------------------------
# Program 30: Display the contents of a string using f-string literals and also using the format () method
'''
name = "Jake"

print("My name is {}".format(name))
print(f"My name is {name}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 31: Display the contents of a string using f-string literals and also using the format () method
'''
name = "Jake"
age = 3

print(f"{name} is {age} years old")
'''
#---------------------------------------------------------------------------------------------------------
