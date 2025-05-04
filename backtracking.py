"""
Backtracking algorithm is based on DFS.
Backtracking is applied to a binary tree. Note that It is not applied to a binary search tree.

backtracking is a brute force approach where you go through every single possibility. In backtracking, we try all possible nodes / solutions
and backtrack when we hit a dead end or the condition to continue is not met.
Is somehow used for path finding.
Can be done recursively.
For example: determine if a path exists from rroot to leaf without hitting a 0.

Recursive Algorithm:
Base case: Either the node is null or the node value does not satisfy the specified condition
Time complexity: O(n) this is because backtracking being a brute force algorithm, we might need to check all nodes.
Space complexity: O(h) h is the height of the tree. This is because we are using recursion.
1. Start at the root.
2. Check for base case. If base case is met then return False
3. Check the pass case. If the pass case is met, return True / or perform some operation.
4. Recursively check the left child. Return true if point 3 is satisfied.
5. Recursively check the right child. Return true if point 3 is satisfied.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def canReachLeaf(root):
    # Check for base case
    if not root or root.val == 0:
        return False
    
    # Check for pass case
    if not root.left and not root.right:
        return True
    
    # Check left sub tree
    if canReachLeaf(root.left):
        return True
    
    # Check right sub tree
    if canReachLeaf(root.right):
        return True
    
    return False

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left):
        return True
    
    if leafPath(root.right):
        return True
    
    path.pop()
    return False
