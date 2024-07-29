#question 3

# module_DictionaryOperations.py

def merging_Dict(*args):
    """
    Function to merge multiple dictionaries.
    """
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict