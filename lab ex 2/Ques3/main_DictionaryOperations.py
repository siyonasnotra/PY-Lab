
# Importing the module_DictionaryOperations module
import module_DictionaryOperations as mdo

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}
dict3 = {'f': 6, 'g': 7, 'h': 8}
dict4 = {'a': 10, 'i': 9}  #Overlapping key with dict1

# Demonstrating merging_Dict function
merged_dict = mdo.merging_Dict(dict1, dict2, dict3, dict4)
print("Merged dictionary:", merged_dict)