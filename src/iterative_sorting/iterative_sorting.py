# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # make a boolean that says if a swap needs to take place
        swap = False
        for n in range(cur_index +1, len(arr)):
            if arr[n] < arr[smallest_index]:
                swap = True
                smallest_index = n
        # TO-DO: swap
        if swap == True:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #make a swap variable that counts how many swaps took place
    swap_count= None
    while swap_count!= 0:
        swap_count = 0
        #compare items to the item in the next index 
        for i in range(0, len(arr) - 1):
            print(arr)
            #if item is smaller than neighbour swap and add 1 to swap
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count+= 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr