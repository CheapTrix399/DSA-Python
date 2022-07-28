#O(n**2)
def bubble_sort(arr):
    for j in range(len(arr)-1,0,-1):
        for i in range(0,j):
            if(arr[i]>arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

#O(n**2)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        pointer = i
        while((pointer>0) & (arr[pointer]<arr[pointer-1])):
            temp = arr[pointer-1]
            arr[pointer-1] = arr[pointer]
            arr[pointer] = temp
            pointer -= 1
    return arr

#O(n**2)
def selection_sort(arr):
    for i in range(1,len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if(arr[min_index]>arr[j]):
                min_index = j
        if(arr[i-1]>arr[min_index]):
            temp = arr[min_index]
            arr[min_index] = arr[i-1]
            arr[i-1] = temp
    return arr

#O(n log(n))
def merge(arr1,arr2):
    i=0
    j=0
    final_arr = []
    while((i<len(arr1)) | (j<len(arr2))):
        if(i<len(arr1)):
            if(j<len(arr2)):
                if(arr1[i]<arr2[j]):
                    final_arr.append(arr1[i])
                    i+=1
                else:
                    final_arr.append(arr2[j])
                    j+=1
            else:
                final_arr.append(arr1[i])
                i+=1
        else:
            final_arr.append(arr2[j])
            j+=1
    return final_arr

def merge_sort(arr):
    if(len(arr)==1):
        return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

#O(n**2)
def partition(arr):
    left = 0
    right = len(arr)-2
    pivot = len(arr)-1
    while(True):
        while(arr[left]<arr[pivot]):
            left += 1
        while(arr[right]>arr[pivot]):
            right -= 1
        if(left>=right):
            break
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    temp = arr[left]
    arr[left] = arr[pivot]
    arr[pivot] = temp
    return [arr,left]

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    else:
        part = partition(arr)
        left = quick_sort(part[0][:part[1]])
        mid = part[0][part[1]]
        right = quick_sort(part[0][part[1]+1:])
        return left+[mid]+right