def merge(left, right):
    # set initial left index
    left_index = 0
    # set initial right index
    right_index = 0
    # the empty sorted list
    sort = []
    # keep adding to the list in order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sort.append(left[left_index])
            left_index += 1
        else:
            sort.append(right[right_index])
            right_index += 1
    # combine the two lists together
    sort += left[left_index:]
    sort += right[right_index:]
    return sort


def merge_sort(array):
    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr1))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
