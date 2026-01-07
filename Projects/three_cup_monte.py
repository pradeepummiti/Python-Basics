# Program 1: Randomly shuffle the contents in a list by mimicing a Three Cup Monte game
'''
def shuffle_list(mylist):
  shuffle(mylist)

  return (mylist)

def player_input_guess():
  input_guess = " "
  while input_guess not in ['0', '1', '2']:
    input_guess = input("Choose either 0 or 1 or 2: ")

  # Typecasting with integer as input function always returns a string
  return int(input_guess)

def guess_verify(shuffle_list, player_input_guess):
  if (shuffle_list[player_input_guess] == "O"):
    print(f"{"Yes, your guess is correct"}")
  else:
    print(f"{"No, your guess is incorrect"}")
    print(f"{shuffle_list}")

# Initialize the list
my_list = [' ', 'O', ' ']

# Shuffle the list
mixed_up_list = shuffle_list(my_list)

# Accept the guess input from the user
guess_input = player_input_guess()

# Verify the guess
check_guess = guess_verify(mixed_up_list, guess_input)
'''
#---------------------------------------------------------------------------------------------------------
