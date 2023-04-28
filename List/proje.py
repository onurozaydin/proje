def flatten(lst):
    flattened_list = []
    for element in lst:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)
    return flattened_list

def reverse_list(lst):
    reversed_list = []
    for element in lst:
        if isinstance(element, list):
            reversed_list.append(reverse_list(element))
        else:
            reversed_list.append(element)
    return list(reversed(reversed_list))

# Örnek kullanım:
lst1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lst2 = [[1, 2], [3, 4], [5, 6, 7]]

print(flatten(lst1)) # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
print(reverse_list(lst2)) # [[[7, 6, 5], [4, 3], [2, 1]]]
