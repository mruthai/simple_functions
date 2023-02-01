"""QUESION 1"""
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# define the function
# create variable to house the collect numbers
# CONSTRAINTS - the collected number need to be less than 10 ( x <= 9)
# Pull numbers <= 9 
# return the numbers <= 9 into the newly created list
# for fun- sort the list for readablity 

def list_below_10(num_list):
    new_list = [ ]
    for number in num_list:
        if number <= 9:
            new_list.append(number)
    new_list.sort()        
    return new_list


brand_new_numbers = [1,11,14,5,8,9,7,3]
print(list_below_10(brand_new_numbers))




"""QUESTION 2"""
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

# l_1 = [1,2,3,4,5,6]
# l_2 = [3,4,5,6,7,8,10]

# identify two lists
# merge the two list
# sort list
# return new list that is sorted

def merge_list(list_one, list_two):
    new_merge_list = list_one + list_two
    #print(f"Unsorted merged list {new_merge_list}")
    new_merge_list.sort()
    return new_merge_list
    

list_one = [1,2,3,4,5,6]
list_two = [3,4,5,6,7,8,10]
print(f"Test new list{merge_list(list_one,list_two)}")