"""
Binary Tree
Binary tree is a tree like data structure.
Mathematically speaking, a binary tree is a connected, undirected graph with no cycles.

Structure:
A binary tree is made up of Nodes like a linked List
Each binary tree node will have a value, and two pointers (Binary means 2 so each node will have 2 pointers).
The pointers are named left and right since its a tree. These will be the left pointer which will be the left branch of the node and the right pointer which will be the right branch of the node.
IN addition to the pointers called right and left pointers. The node which the pointer is pointing to, is called the child of the previous node which is the parent node.
So a node will have 2 pointers, left and right. And these pointers are pointing to the left child and the right child of the parent node.
Each child node will also have it own 2 pointers which can point to another node making it its child or it can also point to NULL.
A node having both pointers pointing to NULL or nothing is called a leaf node. A node having only one child will not be considered a leaf node. For a node to be a leaf node a node has to have both pointers pointing to NULL.

Root Node:
The top node of the binary tree is called the root node. Each binary tree will always have a single root node (top) and leaf nodes (bottom).
Binary tree's are not allowed to have cycles. A node cannot point to another node up in its hierarchy or even adjacent to it (A node cannot point to a parent or its sibling). A node's child will always be a node which is not its sibling or parent.
All nodes in the tree can be reached by the root node.

Leaf Nodes:
Leaf nodes are nodes which have no children.

All nodes have to be connected to each other in a binary tree.
Height:
The height of any node is the number of descendents it has. Start from the node itself, count the number of decendents (child hierarchy) till you reach the leaf node (bottom).
Each side, left and right of the node may have different heights, We consider the bigger number and calculate the longest path (longer / greater descendents) out of the left and right. 
Which ever side has a bigger height is considered as the height of the node. Start counting at 1 or 0.

Depth:
The depth of any node is the number of ancestors it has (parent hierarchy) up to the root node. Start from 1 or 0.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None