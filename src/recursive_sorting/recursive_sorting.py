# print(merge([2, 3], [5, 8]))

# TO-DO: complete the helper function below to merge 2 sorted arrays

# def merge(arr_a, arr_b):
#     total_elements = len(arr_a) + len(arr_b)
#     merged_arr = [None] * total_elements
#     # Declare indices for each sublist
#     a = 0
#     b = 0
#   # bradys for loop
#     for i in range(total_elements):
#         # Check if either list is empty, if so append the other
#         if a >= len(arr_a):
#             merged_arr[i] = arr_b[b]
#             b += 1
#         elif b >= len(arr_b):
#             merged_arr[i] = arr_a[a]
#             a += 1
#         # Otherwise, compare and append the smallest of the two
#         elif arr_a[a] < arr_b[b]:
#             merged_arr[i] = arr_a[a]
#             a += 1
#         else:
#             merged_arr[i] = arr_b[b]
#             b += 1
#     return merged_arr

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [None] * elements
    a = 0
    b = 0
    
    while elements - 1 >=  a + b:
        if a >= len(arrA):
            merged_arr[a + b] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[a + b] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[a + b] =  arrA[a]
            a += 1
        else:
            merged_arr[a + b] =  arrB[b]
            b += 1
    # TO-DO
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1: 
        return arr
    else:
        mid = len(arr) //2
        arr1 = merge_sort(arr[mid:])
        arr2 = merge_sort(arr[:mid])
        return merge(arr1, arr2)

import time
import random
l1 = list(range(10000))
random.shuffle(l1)
l2 = list(range(20000))
random.shuffle(l2)
l3 = list(range(30000))
random.shuffle(l3)
l4 = list(range(40000))
random.shuffle(l4)
l5 = list(range(50000))
random.shuffle(l5)
l6 = list(range(60000))
random.shuffle(l6)
l7 = list(range(70000))
random.shuffle(l7)
l8 = list(range(80000))
random.shuffle(l8)
l9 = list(range(90000))
random.shuffle(l9)
l10 = list(range(100000))
random.shuffle(l10)
shuffled_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
results = []
for shuffled_list in shuffled_lists:
    l_copy = shuffled_list.copy()
    start_time = time.time()
    merge_sort(l_copy)
    end_time = time.time()
    print(f"runtime: {end_time - start_time}")
    results.append(end_time - start_time)

for result in results:
    print(result)

#     # 2. Once you have gotten down to a single element, you have also * sorted * that element
#     # (a single element cannot be "out of order")
    
#     # 3. Start merging your single lists of one element together into larger, sorted sets
#     # 4. Repeat step 3 until the entire data set has been reassembled
#     # return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
