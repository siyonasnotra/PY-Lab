# main_ListOperations.py

# Importing the module_ListFunction module
import Ques1.module_ListFunction as mlf

# Creating lists
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# Using module functions with these lists
print("Even numbers:", even_numbers)
print("Max of even numbers:", mlf.find_max(even_numbers))
print("Min of even numbers:", mlf.find_min(even_numbers))
print("Sum of even numbers:", mlf.calculate_sum(even_numbers))
print("Average of even numbers:", mlf.calculate_average(even_numbers))
print("Median of even numbers:", mlf.calculate_median(even_numbers))
