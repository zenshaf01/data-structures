"""
Learn about logs in math. Generally learn what log base 2 means and how to calculate logs of numbers and what does the operation entail. (diving the number by 2)

Merge Sort:
Keep splitting the array in half until the sub array has only one element. Then recursively sort the sub arrays by merging two at a time. The resulting array will be sorted. (Splitting data structures in two is called divide and conquer)

Merge sort is preferred over insertion sort.
Can be easily solved with two branch recursion


Algorithm:
1. Return if the length of the input array is less or equal to 1
2. Else calculate the middle of the input array
3. Split the input array in half based on the calculated middle (This will give us the left half of the array and the right half of the array)
4. Recursively call mergeSort() on left half <- Solve left first
5. Recursively call mergeSort on right half
6. Merge the two sorted arrays when they return after meeting the base case.

Merging the sub arrays and three pointers:
1. Have one pointer in each of the subarrays, also called merging arrays
2. Have one pointer in the merged array
3. 1 and 2 will result in us having 3 pointers
4. Solving the left part first, Compare elements at pointers in sub arrays 
5. Put the smaller one in the merged array pointer
6. increment pointers involved in merge, this will only be 2 pointers getting updated per merge
7. repeat

Notes: 
* Splitting is happening while going down the recursive chain
* Merging is taking place while coming up the recursive chain


Stability: Stable. You have to code the merge sorter to enforce this. 
Time complexity: n log n (Log n is very quick and efficient than O(n))
Memory complexity: O(n)


"""

def merge_sort(array, start, end):
    # base case: return if there is only one element in the array. 
    if end - start + 1 <= 1:
        return array
    
    # calculate the middle of the input array
    middle = (start + end) // 2

    # recursively call merge sort on left part of the splitted array
    merge_sort(array, start, middle)
    # recursively call merge sort on the right part of the splitted array
    merge_sort(array, middle + 1, end)

    # sort the input array in place using the start, middle and end
    merge(array, start, middle, end)

    return array

def merge(array, start, middle, end):
    # split the input array in to left and right based on indexes
    left =  array[start:middle+1]
    right = array[middle + 1: end + 1]

    # initialize pointers
    i = 0 # pointer for left array
    j = 0 # pointer for right array
    k = start # pointer for input array


    # go through the left and right until they have elements
    while i < len(left) and j < len(right):
        # if left is less than right, assign left to array pointer
        if  left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        # else assign right to array pointer
        else:
            array[k] = right[j]
            j += 1
        # increment k
        k += 1
    
    # if there are any left over elements in the left or right array because if they were of unequal length when they were split
    # We assign the remaining elements into the input array and increment pointers as needed
    # we do this for both arrays since any can have more or less elements than the other
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


array = [5,4,3,2,1]
sorted = merge_sort(array, 0, len(array)-1)