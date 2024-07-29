# module_SetOperations.py

def add_element(s, element):
    s.add(element)

def remove_element(s, element):
    s.discard(element)

def union_intersection(s1, s2):
    return s1 | s2, s1 & s2

def set_difference(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1 <= s2

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    return s1 ^ s2

def power_set(s):
    from itertools import chain, combinations
    s = list(s)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def unique_subsets(s):
    from itertools import combinations
    s = list(s)
    subsets = []
    for r in range(len(s) + 1):
        subsets.extend(combinations(s, r))
    return [set(subset) for subset in subsets]
