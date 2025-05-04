"""
Binary Search Tree:

Binary Search Tree's (BST) are exactly like Binary Tree's (BT). The only difference between them is that BST has a sorted property to them. 
The Sorted property is that for every single node in the BST, every node in the left sub tree will be less than its parent and every node in the right sub tree. And every node in the right sub tree will be greater than its parent and every node in the left sub tree.
BST's generally do not contain duplicates.

Why we need a sorted binary tree ? So that we can search for a value in it in log n time. Remember you can only apply binary search to a sorted data structure.

Since tree's are a recursive data structure, you can use recursion to find an element in the BST. BST will only require one branch recursion since we are only searching for the target value in one of the sub tree's.

Time complexity: n log n (Only if the BST is a roughly balanced tree. a balanced tree is a tree in which every tree, root and sub tree's, the height of the left and right sub tree is same. The height can only have a difference of 1 for a tree to be balanced.)
O(h) where h is the height of the BST root node.
Balanced tree: This is a tree in which the height of left sub tree is equal or 1 less from the height of the right sub tree
Skewed Tree: This is a tree who's height is equal to the number of nodes in the tree

Why do we need a BST when we have a sorted arrays to apply and use binary search with???
The reason is that insertions and deletions in arrays are done in O(n). Whereas in BST's insertions and deletions can also be done in O(log n) time.


Insertion:
The time complexity of inserting and removing from a BST is proportional to the height of the tree. For balanced BST's the time complexity is O(log n). For unbalancedd trees it is O(n)
Space complexity is O(log n) for best case which is the balanced tree. and O(n) for the worst case which is the case of the skewed tree.

For insertion, you can either add nodes as leaf nodes, or add nodes as root nodes. 
Adding as leaf nodes means adding the node as a leaf of an existing root node. This might create an unbalanced tree
Adding as root means adding the node as root node and then making everything else its child. This is the preferred way of inserting in trees. Creates a balanced BST.
Of course this will require you to figure out where to insert it as root node.

Algorithm for insertion of number n as leaf:
1. Start at root node
2. Compare value at root to n.
3. If n is less than root value then go down the left sub tree if it exists. If it does not exist then create a new node (would be leaf in this case since no other nodes exist) and insert at as a left child of the root.
4. If n is greater than root value then go down the right sub tree if it exists. If it does not exist then create a new node (would be leaf in this case since no other nodes exist) and insert at as a right child of the root.
5. Recursively do 1 to 4 till you have inserted at the correct position. Note that the root node will keep changing to whatever node we are looking at / comparing the n with.


Deletion:
The time complexity of inserting and removing from a BST is proportional to the height of the tree. For balanced BST's the time complexity is O(log n). For unbalancedd trees it is O(n)
Space complexity is O(log n) for best case which is the balanced tree. and O(n) for the worst case which is the case of the skewed tree.
1. Find the minimum:
Find the minimum value in the tree. Finding the minimum is to look at the left sub tree and keep going down once you get to the leaf node. 
Since the BST is sorted you can always find the minimum on the left sub tree and this minimum will be the leaf node on the left child sub tree.
2. Removal is broken up into two cases:
Case 1: The node to be removed has 0 or 1 child
0 child:
Compare each node starting from root, with the target node (the one to be removed). 
If target is less than value at node, go down the left sub tree, else go down the right sub tree.
If you have found the node to be removed, Get the next node of that node (Would be null in the case its a leaf node) and then return it to the parent.
Assign the node/null returned to the next left/right of the parent. This will remove the pointer and the removed node will be garbage collected.

1 child:
Compare each node starting from root, with the target node (the one to be removed). 
If target is less than value at node, go down the left sub tree, else go down the right sub tree.
If you have found the node to be removed, Check if left and right pointers are null, If one is null and the other isnt, then we return the non null side child of the node (to be removed) to its parent and assign it to the left/right pointer.
So essentially the parent will now point to the grand child instead of the child.

Case 2: The node has 2 children and it does or does not have grand-children
Compare each node starting from root, with the target node (the one to be removed). 
If target is less than value at node, go down the left sub tree, else go down the right sub tree.
If you have found the node to be removed, replace the node to be removed with one of it children (Choose the left leaf node) and then call the remove again for the child that replaced the removed node.
Take the smallest value from the right sub tree or take the largest value from the left sub tree. You can use the find minimum to get to the smallest value in the right sub tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#insert val at correct position in the BST and then return the root. This inserts the new node as a leaf node.
def insert(root, val):
    # if root is null we know we have reached the correct position to insert the node at.
    if not root:
        return TreeNode(val)
    
    #if value is greater than the value at root then go down the right sub tree
    if val > root.val:
        root.right = insert(root.right, val)
    #if value is less than the value at root then go down the left sub tree
    elif val < root.val:
        root.left = insert(root.left, val)
    # We return the root of the BST. This could happen in two cases, Either the value has been successfully inserted, or the value already exists and we return the node at which the value is.
    return root

# find the minimum value in the BST, returns the node at which that value is
def find_min(root):
    curr = root
    #keep going down till you get to the leaf node. We go down left, since we know the smallest value will always lie somewhere on the left sub tree.
    while curr and curr.left:
        curr = curr.left
    return curr

# remove an element from the BST
def remove(root, val):
    # if root is null we return null
    if not root:
        return None
    
    # if value is greater than root value then go down the right sub tree
    if val > root.val:
        root.right = remove(root.right, val)
    # if value is less than root value then go down the left sub tree
    elif val < root.val:
        root.left = remove(root.left, val)
    else: 
        # If you have found the value see if its a leaf node
        # if it has no left return its right to its parent
        if not root.left:
            return root.right
        #if it has no right return it left to its parent
        elif not root.right:
            return root.left
        # if it has both left and right
        else:
            # determine the min on the right side
            # we do this to make sure when we remove the current removed node is replaced with a value which when inserted would still result in a valid BST (sorted).
            minNode = find_min(root.right)
            # assign the min found to the current root. We are replacing the node to be removed with its min child (child is the left most min child of the right side of the BST)
            root.val = minNode.val
            # call remove again to remove the node form the child hierarchy which has just replaced the target node
            root.right = remove(root.right, minNode.val)
    # return the current root
    return root 

def binary_search_on_bst(root, target):
    # Base case
    if not root:
        return False
    
    # recursively call self if target might lie somewhere in the right sub tree
    if target > root.val:
        return binary_search_on_bst(root.right, target)
    # recursively call self if target might lie somewhere in the left sub tree
    elif target < root.val:
        return binary_search_on_bst(root.left, target)
    # return true since we have found the target. This is also a base case
    else:
        return True


def binary_search_on_bst(root, target):
    if not root:
        return False

    if target > root.val:
        return binary_search_on_bst(root.right, target)
    elif target < root.val:
        return binary_search_on_bst(root.left, target)
    else:
        return True
