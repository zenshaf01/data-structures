"""
Breadth First Search is a search algorithm from Binary Search Trees. just like depth first search.
In depth first search we prioritize depth. In BFS we prioritize breadth.
This means we visit all nodes in one level first before moving on to the next level.

BFS is also called level order traversal. This is because we visit nodes level by level.
BFS is implemented iteratively.

In BFS we traverse the tree level by level.
BFS is to be implemented iteratively while using a Queue.

Algorithm:

1. Start at root node
2. Add root to queue
3. Start a while loop and keep processing while the queue is not empty
4. start another for loop to iterate over the queue elements
5. pop left from the queue (fifo nature in play) (append to queue and then pop from left)
6. process element / print
7. if node has a left child, append it to queue
8. if node has a right child append it to queue
9. Repeat both loops until the range exhausts in the for loop and the queue becomes empty for the while loop.


Time complexity: O(n) Ignore the two nested loops. Its O(n) because we visit each node only once
Space complexity: O(n) where n are the numbr of nodes in the tree.
"""
from collections import deque

class TreeNode:
    def __int__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    # init a queue
    queue = deque()

    # add the root if it exists
    if root:
        queue.append(root)

    level = 0
    # keep iterating until the queue is empty
    while len(queue) > 0:
        print("Level is: ", level)
        # start iterating for the current length of the queue
        # keep in mind that len of queue in range call is fixed at every level
        for i in range(len(queue)):
            # get the element from the front of the queue. 
            # This means the element was popped and is not not in the queue.
            curr = queue.popleft()
            # process popped element
            print("Processing: ", curr.val)
            
            # if current has left, append it to queue
            if curr.left:
                queue.append(curr.left)
            # if current has right, append it to queue
            if curr.right:
                queue.append(curr.right)
        level += 1
    return level