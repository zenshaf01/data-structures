'''
The heap is tree based data structure. It is sometimes called the priority queue.
The heap / priority queue is a bit different than a queue which is a FIFO data structure. 
The heap removes values based on the specific priority. The element with the highest priority is removed first regardless the order it was added in.
The element with the highest priority will be removed first.

The heap structure is a full binary tree. by full we mean every lervel is copmlete except the last one.
There are 2 types of heaps:
1. Min Heap: In this heap both children (left and right) is greater than or equal to the parent. Min heap has the smallest value at the root node. 
    In a min heap, the smallest value has the highest priority to be removed.
2. Max Heap: Both child nodes are less than or equal to the parent node. Max heap has the largest value at the root node. 
    In a max heap, the largest value has the highest priority to be removed.

Heap Properties:

1. Structure property: A binary heap is a binary tree which is a complete
binary tree. This means that every level is filled, except thee lowest level node,
which are filled contiguously from left to right.

2. Order property: in a min heap, every descendent in the left and right sub tree, should be greater
or equal to their ancestor. In a max heap, every descendent is smaller or 
equal than or equal to it ancestor.

3. Heaps may contain duplicate values. This is opposit to the binary search tree.
    
Notes:
- Binary heaps are conceptually drawn like a tree data structure but internally
they are implemented using arrays.

- For the above, the array that is to contain the binary heap elements is initialized with a size
 of n + 1, Where n is the num elements. When populating the array, we visit nodes using
 breadth first search, level by level, left to right. 
 But we start filling the array from index 1 instead of index 0. 
 We do this so that we can easily figure out the index of a nodes parent, left child and right child. this is also the reason we initialize the array with teh size of n + 1.
 The following is the formulas for that:
    1. parent = i / 2 (i is index of node for which the parents index is to be found)
    2. left child = 2 * i (i is index of node for which the left childs index is to be found)
    3. right child = 2 * i + 1 (i is index of node for which the right childs index is to be found)

 The above formulas only work if the tree is a complete binary tree and the array is filled conriguously from left to right.

 Operations:
 Each operation performed on the heap must ensure that the heap property's are maintained even after the operation is performed.
 Each operation should adhere to the structure and the order property. Meaning for example if an element is being pushed on to the heap, 
 it must be firstly added contiguosly meaning added to the next correct position at the last available level, 
 but at the same time the push should also make sure that the order property is also maintained and 17 is added in a way that the order property is preserved.
 The order property can be preserved by bubbling or percolating the element up the tree till it gets to the correct position.

 Bubbling / Percolation algorithm:
    1. Add the elelemt pushed to the next available contiguous position in the heap.
    2. Compare the added element with its parent.
    3. If the new element is less than its parent (in min heap, it should be opposite in the max heap), swap the new element with its parent.
    4. Repeat 2 and 3 until the new element is in the correct spot in the heap (You will know this when the comparison fails at 2 and 3 and 4 are not run)

 Read: Reading from a min or max heap can be done in constant time O(1).
 Push: 
    1. Add the new element in the next contiguous location in the array / heap.
    2. Perform the bubbling algorithm to bring the new element to the correct position based on the type of heap.
 Pop:
    Since we remove the element with the highest priority, 
    which will always be at the top of the heap, the order property will be preserved bu then the structure property is not preserved.
    Which is why popping is not as trivial as it may seem.

    1. Save the root element in a result variable
    2. swap the right most node of the last level with teh root node. this will mean just assign the last element of the array to the index 1
    3. keeps swapping the new root (which might be in the incorrect position) with the min(left, right) or max(left, right) to bring the new root to the correct position.
        We do this by
        a. as long as there is a left child run a loop
            if there is a right and the right is less than the left and the current is grerater than the right. swap current with right
            else if current is greater than the left, swap with left
        b. we replace the root with the minimum of the left and right children (Note that if there is a right child, there will always be a left child for a heap to be a complete bionary tree)


'''

class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        # add element to next available contiguous position
        self.heap.append(val)
        i = len(self.heap) - 1

        # bubbling / percolating for min heap. For max heap the condition will change to check if new element is greater than its parent.
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        # if length is 1 we know the heap is empty
        if len(self.heap) == 1:
            return None
        
        # if length is 2 we know that teh heap has only 1 element wont require swaps
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # save the result
        result = self.heap[1]

        # bring right most element of the last level to root
        self.heap[1] = self.heap.pop()

        i = 1

        # while there is a left
        while i * 2 < len(self.heap):
            # if there is a right and the right is less than the left and the current at i is greater than right
            if (i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i] > self.heap[i * 2 + 1]):
                # swap
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                # go to the right sub tree
                i = 2 * i + 1
            # if current is larger than left
            elif self.heap[i] > self.heap[2 * i]:
                # swap
                tmp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = tmp
                # go to the left sub tree
                i = 2 * i
            else:
                break

        return result
