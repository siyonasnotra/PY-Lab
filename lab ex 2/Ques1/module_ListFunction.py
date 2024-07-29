def find_max(lst):
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    if  not lst:
        return None
    return min(lst)

def calculate_sum(lst):
    if not lst:
        return None
    return sum(lst)

def calculate_average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def calculate_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_lst[middle - 1] + sorted_lst[middle]) / 2
    else:
        return sorted_lst[middle]

# Test code (to be removed or commented out in the actual module)
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print("Max:", find_max(sample_list))
    print("Min:", find_min(sample_list))
    print("Sum:", calculate_sum(sample_list))
    print("Average:", calculate_average(sample_list))
    print("Median:", calculate_median(sample_list))

