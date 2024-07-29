# main_SetOperations.py

# Importing the module_SetOperations module
import module_SetOperations as mso

# Example sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {4, 5, 6}

# Demonstrating add_element function
mso.add_element(set1, 4)
print("After adding element to set1:", set1)

# Demonstrating remove_element function
mso.remove_element(set1, 4)
print("After removing element from set1:", set1)

# Demonstrating union_intersection function
union, intersection = mso.union_intersection(set1, set2)
print("Union of set1 and set2:", union)
print("Intersection of set1 and set2:", intersection)

# Demonstrating set_difference function
difference = mso.set_difference(set1, set2)
print("Difference set1 - set2:", difference)

# Demonstrating is_subset function
is_subset_result = mso.is_subset(set1, set2)
print("Is set1 a subset of set2?", is_subset_result)

# Demonstrating set_length function
length = mso.set_length(set1)
print("Length of set1:", length)

# Demonstrating symmetric_difference function
symmetric_diff = mso.symmetric_difference(set1, set2)
print("Symmetric difference of set1 and set2:", symmetric_diff)

# Demonstrating power_set function
power_set_result = mso.power_set(set1)
print("Power set of set1:", power_set_result)

# Demonstrating unique_subsets function
unique_subsets_result = mso.unique_subsets(set1)
print("Unique subsets of set1:", unique_subsets_result)
