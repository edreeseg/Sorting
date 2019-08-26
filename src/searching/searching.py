# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if (arr[i] == target):
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
  low = 0
  high = len(arr)-1
  # TO-DO: add missing code
  while (low <= high):
    current = (high+low)//2
    if (arr[current] == target):
      return current
    elif (arr[current] > target):
      high = current - 1
    else:
      low = current + 1
  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if low > high:
    return -1
  middle = (low+high)//2
  print(f'Middle is {middle}')
  if arr[middle] == target:
    return middle
  return binary_search_recursive(arr, target, low, middle-1) if arr[middle] > target else binary_search_recursive(arr, target, middle+1, high)

test = [1, 3, 5, 6, 7, 8, 9, 10, 11, 14, 17, 22]
print(binary_search_recursive(test, 11, 0, len(test)-1))