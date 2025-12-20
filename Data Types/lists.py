# Program 1: Determine the length of a list 
'''
my_list = ['Alice', 100, 5.7]

print(f"The length of the list is: {len(my_list)}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 2: Determine the object at index 2 using list indexing concept
'''
my_list = ['Alice', 100, 5.7]

print(f"The object at index 2 from the list is: {my_list[2]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 3: Display all the objects in the list from index till the end using list slicing concept
'''
my_list = ['Alice', 100, 5.7, 'one', 'two', 'three']

print(f"The list starting from index till the end is: {my_list[1:]}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 4: Concatenate more than one list
'''
list1 = ['Alice', 100, 5.7]
list2 = ['one', 'two', 'three']

list_concatenate = list1 + list2

print(f"The first list is: {list1}")
print(f"The second list is: {list2}")
print(f"The concatenated list is: {list_concatenate}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 5: Modify any object in a list
'''
my_list = ['Alice', 100, 5.7]

print(f"The original list is: {my_list}")
my_list[1] = 'ONE'
print(f"The modified list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 6: Add a element at the end of a list using "append" method
'''
my_list = ['Alice', 100, 5.7]

print(f"The original list is: {my_list}")
my_list.append('ONE')
print(f"The modified list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 7: Remove an element from the end of a list using "pop" method
'''
my_list = ['Alice', 100, 5.7, 'ONE']

print(f"The original list is: {my_list}")
popped_item = my_list.pop()
print(f"The modified list is: {my_list}")
print(f"The deleted or popped item from the list was: {popped_item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 8: Remove an element from a specific index from the list
'''
my_list = ['Alice', 100, 5.7, 'ONE']

print(f"The original list is: {my_list}")
popped_item = my_list.pop(1)
print(f"The modified list is: {my_list}")
print(f"The deleted or popped item from the list was: {popped_item}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 9: Sort the items for a list, assign the sorted list to a new variable and check its type
'''
my_list = ['a', 'b', 'x', 'p', 'e', 'm']

print(f"The original list is: {my_list}")
popped_item = my_list.sort()
print(f"The modified list is: {my_list}")
print(f"The content of the assignment is: {popped_item}")
print(f"The type of the assignment is: {type(popped_item)})")
'''
#---------------------------------------------------------------------------------------------------------
# Program 10: Sort the items for a list of numbers in ascending order
'''
my_list = [3, 50, 25, 6, 100, 99]

print(f"The original list is: {my_list}")
my_list.sort()
print(f"The modified list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
# Program 11: Reverse the items for a list
'''
my_list = [3, 50, 25, 6, 100, 99]

print(f"The original list is: {my_list}")
my_list.sort()
print(f"The modified list is: {my_list}")
'''
#---------------------------------------------------------------------------------------------------------
