# Program 1: Open a txt file
'''
my_file = open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Read a file
'''
my_file = open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt")
my_file.read()
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Seek a file from the beginning of the file after a read operation
'''
my_file = open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt")
my_file.read()
my_file.seek(0)
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Display each line in a file as an object of a list
'''
my_file = open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt")
my_file.readlines()
my_file.seek(0)
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Close a file that was opened previously
'''
my_file = open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt")
my_file.readlines()
my_file.seek(0)
my_file.close()
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Append a new line to existing file contents
'''
with open("C:\\Users\\pradeepummiti\\Downloads\\myfile.txt", mode = 'a') as my_file:
  my_file.write('\nFOUR')  
my_file.readlines()
my_file.seek(0)
my_file.close()
'''
#---------------------------------------------------------------------------------------------------------
