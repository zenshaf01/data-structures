"""
Quick Sort

The quick sort algorithm is also a divide and conquer algorithm to sort lists. Similar to the merge sort.
In Quick sort we select a pivot which is an index of the input array and then partition (split) the array such that,
all elements to the left of the array are less than the element at pivot and all right elements are greater than the pivot element.
Quick sort does not require extra memeory like merge sort because we arte not creating a new array for it, sorting is done in place.
Quick sort is not a stable sorting algorithm like merge sort. The original relative order of duplicate values will not be preserved.

you can pick a pivot from the following:
1. pick the first index
2. pick the last index
3. pick the median index
4. pick a random index

The most efficient sorting can be achieved if we pick a pivot which divides the list in equal halves. 
But you can pick the pivot based on any of the above. You can also pick the last index just for simplicity.

Algorithm:

Recursive solution
base case: input list has only 1 element.

1. Select th pivot index
2. Start iterating over the array
3. Compare each element of the array with the pivot.
4. If element is less than value at pivot, place element in the left partitioned array (Same array -> all operations are done in place)
5. If element is greater thban value at pivot, place element in the right partitioned array (Same array -> all operations are done in place)
Note on 4 and 5:
4 and 5 are done in the following:
1. maintain one pointer i in for the iteration, and one pointer j to maintain insertion location.
2. if element at i is less than or equal to pivot, swap element at i with element at j and then increment j, else we dont do anything and move pointer i to next location (i + 1). We dont move the insertion pointer j.
3. if i has reached pivot, we will swap element at pivot with j
4. Repeat recursively from step 1 of algorithm untill it reaches the base case.
Note that as we keep splitting (partitioning) the array the pivot keeps becoming the last value of the new splitted (partitioned) array.

Time complexity: 
* n^2 for worst case
* n log n if pivot is middle value (average)

"""
def quick_sort(arr, s, e):
    # base case
    if e - s + 1 <= 1:
        return arr
    
    # set pivot and left (left is the insertion pointer)
    pivot = arr[e]
    left = s

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        # if i is less than pivot swap i with left
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    
    # when i reaches pivot, swap pivot with left
    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sort left side
    quick_sort(arr, s, left - 1)
    # quick sort right side
    quick_sort(arr, left + 1, e)

    return arr

array = [5,4,3,2,1]
sorted = quick_sort(array, 0, len(array)-1)
print(sorted)