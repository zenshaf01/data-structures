"""
Binary Search:

it is an algorithm to search for items in a sorted array.
Binary search only works on a sorted array.
binary search divides a given array by the middle index, called mid and compares the value at mid to the target value. 
If the target is greater than the mid value, we will search the right half of the array. If the target is less than the mid value, we will search the left half of the array.

Algorithm:

1. Set the boundaries for input array. Left is the start of the array and Right is the end of the array. (This is the search space where have to look for the target element)
2. Add Left and Right index and divide the result with two (arr[l] + arr[r] / 2). This will get us the middle point (Middle index) of the array. If the result of the formula is a floating point number we round it down.
3. Start iterating with a while loop and check if L is less or equal to right. The loop will keep executing even if L and R at the same position.
4. Calculate the mid
5. If target is greater than the value at Middle index, set the new Left to be Middle point + 1, This means we have determined that the target lies somewhere to the right og the middle point.
6. If target is less than the value at Middle index, Set the new Right  to be the Middle - 1. This means we have determined that the target lies somewhere to the left of the middle point.
7. Goto 3 if 5 or 6 are true
8. If 5 or 6 both are false, then it means we have found the target, we return Middle index.
9. If the loop has exited and we did not find the target that means the target does not exist in the array, we return -1.

Time complexity:
Worst case: n log n

"""
def binary_search(arr, target):
    # init left and right pointers, setting the search space
    left, right = 0, len(arr) - 1

    # keep iterating until left goes past right
    while left <= right:
        # calculate mid point
        mid = left + ((right - left) // 2)

        # if target is greater than value at mid point then target lies somewhere right, reset left to next of middle pointer
        if target > arr[mid]:
            left = mid + 1
        # if target is less than value at mid point then target lies somewhere left, reset right to previous of middle pointer
        elif target < arr[mid]:
            right = mid - 1
        # if previous two are false that means we have foound the target
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6]
target = 6
found = binary_search(arr, target)
print('found: ', found)

def binary_search(arr, target):
    # set the start and end
    left, right = 0, len(arr) - 1

    # start iterating until the left and right pointers cross each other
    while left <= right:
        # calculate middle
        mid = ((right - left) // 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return arr[mid]
    return -1
