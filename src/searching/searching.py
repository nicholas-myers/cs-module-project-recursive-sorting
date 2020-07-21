# TO-DO: Implement a recursive implementation of binary search
import math

def binary_search(arr, target, start, end):
    # Your code here
    # if the array is empty return -1
    if len(arr) == 0:
        return -1
    # get mid point
    mid = math.floor((end + start) / 2)
    print(mid)
    
    # return index if target is equal to mids value
    if target == arr[mid]:
        return mid
    # or right if greater than
    if target > arr[mid]:
        # change the start
        new_start = mid
        return binary_search(arr, target, new_start, end)
    # go left target is less than the mid 
    if target < arr[mid]:
        # change the end
        new_end = mid        
        return binary_search(arr, target, start, new_end)
    
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, 1, 0, len(arr1)-1)
