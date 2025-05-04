"""
Queues are similar to Arrays.
Queues are also similar to Stacks.
Queues follow First In First Out (FIFO) rule.

Think of queues to be like real life queues / lines. The first person who enters the line will be the first one to be served. 

The easiest way to implement Queues is to use a linked list. This ensures O(1) time complexity.
It can also be implemented with arrays but this leads to O(n) operation because we would have to shift all the elements for each operation.

Operations:
1. enqueue: Means to add an element to the end (tail) of the queue. Time complexity is O(1) if using linked list.
    Linked list enqueue algorithm:
        1. Create new node
        2. If List is empty, assign new node to be the left (head) and right (tail) of the queue
        3. If List is not empty, assign the new node to the next of the right (tail) and then set the new node (right.next) to be the new right (tail)
2. dequeue: Means to remove an element (val) from the front (head) of the queue. Time complexity is O(1) if using linked List.
    Linked list dequeue algorithm:
        1. Check if queue is empty, return null if it is
        2. Get the value for the left (head) most element
        3. set left.next to be the new left (head).
        4. If left (head) now is null, set right (tail) to be null as well  
"""
# Queue implemented with a linked list
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def enqueue(self, val):
    newNode = ListNode(val)

    # If list is not empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    #else list is empty
    else:
        self.left = self.right = newNode

def dequeue(self):
    if not self.left:
        return None
    
    #remove left node and return value
    val = self.left.val
    self.left = self.left.next

    # if the new left is null that means the right was null as well so set it to null explicitely
    if not self.left:
        self.right = None
    return val