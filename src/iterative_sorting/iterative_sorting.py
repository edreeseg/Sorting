# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if (arr[i] > arr[i+1]):
                done = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    count = [] if maximum == -1 else [0] * (maximum + 1)
    for n in arr:
        try:
            count[n]+=1
        except IndexError:
            count.extend([0] * (n-len(count)) + [1])
    sum = 0
    for i in range(len(count)):
        sum += count[i]
        count[i] = sum
    count.insert(0, 0)
    del count[-1]
    result = [0] * len(arr)
    for n in arr:
        result[count[n]] = n
        count[n]+=1
    return result

print(count_sort([], 0))

# EXTRA: insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr.pop(i)
        decr_index = i-1
        while current_value < arr[decr_index] and decr_index >= 0:
            decr_index-=1
        arr.insert(decr_index+1, current_value)
    return arr
