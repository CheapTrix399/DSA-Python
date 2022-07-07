from sorting import merge_sort

def linear_search(value,array):
    for i in range(len(array)):
        if(array[i]==value):
            return i
    return None

def binary_search(value,array):
    if(len(array)==0):
        return False
    array = merge_sort(array)
    mid = int(len(array)-1/2)
    if(array[mid]==value):
        return True
    else:
        left = binary_search(value,array[:mid])
        right = binary_search(value,array[mid+1:])
        return left | right