"""
Bucket Sort:

Bucket sort can only be used if the values we are sorting fit within a finite range.
In bucket sort we create a bucket for each value, This can be just a normal place in a new array for that value. Each value is mapped to the new arrays index and that index is initialized with a value of 0 (the number of times that values comes up.)
And then we count the number times that particular value showes up in the original array and we keep incrementing the number of times it does show up by incrementing the value (which was initialized to 0 in previous step) for the target index by 1.
Very rarely usable.
Mostly forbidden.

Algorithm:
1. Initialize a new array which will act as a bucket for the frequencies of items present in the input array
2. Start iterating over the input array and add the frequencies for the items to the mapped bucket in bucket array
3. Start iterating overt the bucket and put the item in the input array equal to the frequency times for that item. Meaning if 2 has a frequency of 1 you will put 2 in input array 1 times.

Stability: It is not a stable sorting algorithm.
Time complexity: 
Worst case O(n)

"""
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    max_val = max(arr)
    counts = [0] * (max_val + 1)  # Initialize counts list with zeros

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

array = [5,6,7,8,9,2,24,5]
sorted = bucketSort(array)
print(sorted)