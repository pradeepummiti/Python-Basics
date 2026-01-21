# Program 1: Write a function that returns the lesser of two numbers if both numbers are even, but 
# returns the greater of the two numbers if either of the numbers is odd
'''
def lesser_of_two_evens(num1, num2):
  if ((num1 % 2 == 0) and (num2 % 2 == 0)):
    if (num1 < num2):
      return num1
    else:
      return num2
  elif ((num1 % 2 != 0) or (num2 % 2 != 0)):
    if (num1 > num2):
      return num1
    else:
      return num2

result_num = lesser_of_two_evens(2, 4)
print(f"The value of result is: {result_num}")

result_num = lesser_of_two_evens(2, 5)
print(f"The value of result is: {result_num}")

result_num = lesser_of_two_evens(9, 7)
print(f"The value of result is: {result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Write a function that takes two word string and returns True if both words begin with the 
# same letter
'''
def animal_crackers(word_text):
  word_split = word_text.split()

  first_word = word_split[0][0].lower()
  second_word = word_split[1][0].lower()

  if (first_word == second_word):
    return True
  else:
    return False
  
result_text = animal_crackers("Levelheaded Llama")
print(f"The value of result is: {result_text}")

result_text = animal_crackers("Crazy Kangaroo")
print(f"The value of result is: {result_text}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Write a function that returns the value of a given number that is twice far away as the other
# side of seven
'''
def other_side_of_seven(num):
  dist = num - 7
  sym_dist = dist * -2
  res_dist = sym_dist + 7
  
  return res_dist
  
result_num = other_side_of_seven(4)
print(f"The value of result is: {result_num}")

result_num = other_side_of_seven(10)
print(f"The value of result is: {result_num}")

result_num = other_side_of_seven(12)
print(f"The value of result is: {result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Write a function that capitalizes the first and fourth letter of a name
'''
def old_macdonald(name):
  first_part = name[0].upper()
  second_part = name[1:3]
  third_part = name[3].upper()
  last_part = name[4:]

  return first_part + second_part + third_part + last_part
  
result_name = old_macdonald("macdonald")
print(f"The value of result is: {result_name}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Write a function that takes a sentence and reverses the words of the sentence
'''
def master_yoda(sentence):
  words = sentence.split()        
  words.reverse()                 
  reversed_sentence = " ".join(words) 
  return reversed_sentence

  return first_part + second_part + third_part + last_part
  
result_sentence = master_yoda("I am home")
print(f"The value of result is: {result_sentence}")

result_sentence = master_yoda("We are ready")
print(f"The value of result is: {result_sentence}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Write a function that returns True if an integer is within 10 of either 100 or 200
'''
def almost_there(num):
  if ((90 <= num <= 110) or (190 <= num <= 210)):
    return True
  else:
    return False

result_num = almost_there(90)
print(f"The value of result is: {result_num}")

result_num = almost_there(104)
print(f"The value of result is: {result_num}")

result_num = almost_there(150)
print(f"The value of result is: {result_num}")

result_num = almost_there(209)
print(f"The value of result is: {result_num}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Write a function that counts the number of times a given pattern appears in the string, 
# including overlap
'''
def laughter(text, pattern):
  count = 0
  start = 0
  
  while True:
    try:
      index = text.index(pattern, start)
      count += 1
      start = index + 1
    except ValueError:
      break

  return count
    
result_count = laughter("hahahah", "hah")
print(f"The value of result is: {result_count}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Write a function that returns a string where for every character in the original string there
# are three characters
'''
def paper_doll(text):
  result_char = " "
  for char in text:
    result_char = result_char + char*3
  return result_char
    
result_text = paper_doll("Hello")
print(f"The value of result is: {result_text}")

result_text = paper_doll("Mississippi")
print(f"The value of result is: {result_text}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Write a function that given three integers between 1 and 11, if their sum is less than or 
# equal to 21, return their sum. If their sum is greater than 21 and if there is 11, reduce the total sum
# by 10. Finally, if the sum (even after adjustment) is greater than 21, return "BUST"
'''
def blackjack(n1, n2, n3):
  if ((1 <= n1 <= 11) and (1 <= n2 <= 11) and (1 <= n3 <= 11)):
    if (n1 + n2+ n3 <= 21):
      return n1 + n2 + n3
    elif ((n1 + n2+ n3 > 21) and ((n1 == 11) or (n2 == 11) or (n3 == 11))):
      return n1 + n2 + n3 - 10
    elif (n1 + n2+ n3 > 21):
      return "BUST"
      
result_sum = blackjack(5, 6, 7)
print(f"The value of result is: {result_sum}")

result_sum = blackjack(9, 9, 9)
print(f"The value of result is: {result_sum}")

result_sum = blackjack(9, 9, 11)
print(f"The value of result is: {result_sum}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Write a function that returns the sum of numbers in an array, except ignore sections of
# numbers starting with a 6 and extending to the next 9 (every 6 will be followed by atleast one 9).
# Return 0 if no numbers
'''
def summer_69(arr):
  total = 0
  add = True
  for num in arr:
    while add:
      if num != 6:
        total = total + num
        break
      else:
        add = False
    while not add:
      if num != 9:
        break
      else:
        add = True
        break

  return total

result_sum = summer_69([1, 3, 5])
print(f"The value of result is: {result_sum}")

result_sum = summer_69([4, 5, 6, 7, 8, 9])
print(f"The value of result is: {result_sum}")

result_sum = summer_69([2, 1, 6, 9, 11])
print(f"The value of result is: {result_sum}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Write a function that returns True when the sum of two integers is 20, or if one of the
# integers is 20. If not, return False
'''
def makes_twenty(num1, num2):
  if ((num1 + num2 == 20) or (num1 == 20) or (num2 == 20)):
    return True
  else:
    return False
  
result_sum = makes_twenty(20, 10)
print(f"The value of result is: {result_sum}")

result_sum = makes_twenty(12, 8)
print(f"The value of result is: {result_sum}")

result_sum = makes_twenty(2, 3)
print(f"The value of result is: {result_sum}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 12: Write a function that returns True if there is a 3 next to a 3 in a list of integers
'''
def has_33(list_num):
  for i in range(0, len(list_num)-1):
    if ((list_num[i] == 3) and (list_num[i+1] == 3)):
      return True
  return False
  
result_list = has_33([1, 3, 3])
print(f"The value of result is: {result_list}")

result_list = has_33([1, 3, 1, 3])
print(f"The value of result is: {result_list}")

result_list = has_33([3, 1, 3])
print(f"The value of result is: {result_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 13: Write a function that accepts a list of integers and returns True if it contains 007 in 
# order
'''
def spy_game(list_num):
  order_list = [0, 0, 7, "x"]
  for i in list_num:
    if (i == order_list[0]):
      order_list.pop(0)
  return len(order_list) == 1
  
result_list = spy_game([1, 2, 4, 0, 0, 7, 5])
print(f"The value of result is: {result_list}")

result_list = spy_game([1, 0, 2, 4, 0, 5, 7])
print(f"The value of result is: {result_list}")

result_list = spy_game([1, 7, 2, 0, 4, 5, 0])
print(f"The value of result is: {result_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 14: Write a function that returns the number of prime numbers that exist and upto and including
# a given number
'''
def count_primes(num):
  if (num < 2):
    return 0
    
  # Store the prime numbers
  primes = [2]

  # Counter going upto the input number
  x = 3

  # x is going through every number upto the input number
  while (x <= num):
    # Check if x is prime
    for y in range (3, x, 2):
      if (x % y == 0):
        x = x + 2
        break
    else:
      primes.append(x)
      x = x + 2

  print(f"{primes}")

  return len(primes)
      
result_prime = count_primes(100)
print(f"The value of result is: {result_prime}")
'''
#---------------------------------------------------------------------------------------------------------
