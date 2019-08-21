# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if arrA == []:
            merged_arr[i] = arrB.pop(0)
        elif arrB == []:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])
    return merge(left, right)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# EXTRA quicksort
def partition(l):
    left, right, pivot = [], [], l[0]
    for n in l[1:]:
        if n > pivot:
            right.append(n)
        elif n < pivot:
            left.append(n)
    return left, right, pivot
def quicksort(l):
    if len(l) <= 1:
        return l
    left, right, pivot = partition(l)
    return quicksort(left) + [pivot] + quicksort(right)
