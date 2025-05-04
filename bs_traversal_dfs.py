"""
Binary Search Tree traversal (search) with depth first search (DFS)
Time complexity: O(n)

DFS: Go to the depth of the tree first (reach the bottom / leaf node) and then process the source node. That is why its called depth first.
DFS is in contrast to breadth first search which is BFS, in which we process the tree layer by layer.

Like we do searches on arrays, which is left to right. Ther same can be done with BST's. 
This will involve going from left to right. This BST traversal (search) in sorted order is also called inorder traversal.
It would be a recursive function going through the BST in order. 

In order Algorithm:
Recursive solution,
1. Start at root
2. If has left child go down.
3. Keep going down left till you reach a node with no children (is leaf node)
4. Process leaf (smallest) node
5. Go back up to parent
6. Process parent
7. If has right child go down. 
8. Keep going down left in the right sub tree till you reach leaf node
9. Process left leave
10. Pop back up and process.
11. Repeat 

in simple words DFS is for a node recursively check and go down left till you encounter leaf and then process left first, then go back up process parent / root then check and go down right and repeat.
For each node you encounter you go down left first, process left and then process parent and then go down right. repeat.

First we have to get to the left most leaf node (This would be the smalles value in the BST). 
One the left side is processed, we go down the right sub tree of the node, after processing the right we pop backl up to the parent node.
And the process as same goes on till we reach the node. After reaching root we go down the right sub tree. Doing left first processing on all descendent sub trees.

Time complexity:
Worst case: O(n)
But if we get an un sorted input array, We can build the BST using the insertion algorithm and then apply search on the sorted BST. This will make the time complexity be O(n log n)

Preorder Traversal Algorithm:
1. Visit and process parent first
2. Visit and process left sub tree
3. Visit and process right sub tree

Postorder Traversal Algorithm:
1. Visit and process left sub tree
2. Visit and process right sub tree
3. Visit and process parent first
"""

def inorder_left_first(root):
    # if reached leaf return none
    if not root:
        return None
    #go down the left sub tree
    inorder_left_first(root.left)
    #process current node
    print(root.val)
    # go down the right sub tree
    inorder_left_first(root.right)

def inorder_right_first(root):
    # if reached leaf return none
    if not root:
        return None
    # go down the right sub tree
    inorder_right_first(root.right)
    #process current node
    print(root.val)
    #go down the left sub tree
    inorder_right_first(root.left)

 
def preorder(root):
# if reached leaf return none
    if not root:
        return None
    #process current node
    print(root.val)
    #go down the left sub tree
    preorder(root.left)
    # go down the right sub tree
    preorder(root.right)

def postorder(root):
# if reached leaf return none
    if not root:
        return None
    #go down the left sub tree
    postorder(root.left)
    # go down the right sub tree
    postorder(root.right)
    #process current node
    print(root.val)


