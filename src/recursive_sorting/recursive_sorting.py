# print(merge([2, 3], [5, 8]))

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    while elements >  0:
        if len(arrA) == 0:
            merged_arr[len(merged_arr) - elements] = arrB.pop(0)

        elif len(arrB) == 0:
            merged_arr[len(merged_arr) - elements] = arrA.pop(0)

        else:    
            if arrA[0] < arrB[0]:
                merged_arr[len(merged_arr) - elements] = arrA.pop(0)

            else:
                merged_arr[len(merged_arr) - elements] = arrB.pop(0)
        elements = len(arrA) + len(arrB)
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

    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also * sorted * that element
    # (a single element cannot be "out of order")
    
    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
