import math
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    print(merged_arr)
    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if the array is more than 1 item sort
    main = []
    if len(arr) > 1:
        # find the midpoint
        mid = math.floor(len(arr)/2)
        # print(mid)
        # split into two arrays
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        # print(left)
        # print(right)
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # left starting point
        leftstart=0
        # right starting point
        rightstart=0
        # main arr start
        main=0
        # go through left and right and put in order to main
        while leftstart < len(lefthalf) and rightstart < len(righthalf):
            if lefthalf[leftstart] <= righthalf[rightstart]:
                arr[main]=lefthalf[leftstart]
                leftstart=leftstart+1
            else:
                arr[main]=righthalf[rightstart]
                rightstart=rightstart+1
            main=main+1

        while leftstart < len(lefthalf):
            arr[main]=lefthalf[leftstart]
            leftstart=leftstart+1
            main=main+1

        while rightstart < len(righthalf):
            arr[main]=righthalf[rightstart]
            rightstart=rightstart+1
            main=main+1
                
        
    # if the array is empty or only has one item return the array as is
    
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
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
