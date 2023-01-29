def binary_search_string(values, target):
    start = 0
    end = len(values) - 1

    while start <= end:
        middle = (start + end) // 2
        midpoint = values[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint


def binary_search_int(values, target):
    low_num = 0
    upp_num = len(values) - 1
    while values[low_num] <= values[upp_num]:
        mid_num = (low_num + upp_num) // 2
        if values[mid_num] < target:
            low_num = mid_num + 1
        elif values[mid_num] > target:
            upp_num = mid_num - 1
        else:
            return mid_num


def binary_search(values, target):
    if isinstance(target, str):
        return binary_search_string(values, target)
    elif isinstance(target, int):
        return binary_search_int(values, target)


