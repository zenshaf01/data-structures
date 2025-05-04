"""
Insertion Sort:
Insertion sort is a stable sorting algorithm. It sorts the array of elements by looking at the left side of the array for each individual element and then keeps making necessary swaps if the left side is greater than the right side.
It is best done in an iterative manner.
Note that you can code it to be an unstable sorting algo but that is not recommended.
Stable sorting algo's do not make the swap if the elements being compared are equal.

in simple words, for each element i of array, you try to figure out if it needs to move left or not depending if it smaller or not. or in other words if the lft is greater than the right. 
A passthrough is each element being checked against its left side to place it in the correct spot, number of passthroughs would be equal to length of list.

Time Complexity:
Best Case: O(n) <- when list is already sorted. Linear time
Worst case: O(n^2)

Algorithm:
1. Start first loop at index 1 of array <- First loop
2. Check the left side of the array for each element. <- Second loop
3. If left is greater than right, then swap left and right. Keep doing this step till you reach the beginning of the array.
4. go to next index
5. repeat from 2


There are two types in sorting algorithms.
1. Stable Sorting: Preserves order for duplicated values.
2. Unstable Sorting: Order is not guaranteed for duplicated values.

Can be done recursively (Breaking it into sub problems) as well as iteratively.
"""

def insertion_sort(array):
    # start from 1st index to end of array
    for i in range(1, len(array)):
        # start inner loop with j being 1 less than i
        j = i - 1
        # keep executing if j hasnt gone out of bounds and element at j (left) is greater than element at j + 1 (right)
        while j >= 0 and array[j] > array[j + 1]:
            # save right as temp
            temp = array[j + 1]
            # assign left to right position
            array[j + 1] = array[j]
            # assign tempt ot left position
            array[j] = temp
            # decrement j
            j -= 1
    return array

array = [5,4,3,2,1]
sorted = insertion_sort(array)
print('sorted array: ', sorted)
