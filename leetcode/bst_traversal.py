# Recursive solution:
def inorderTraversalRecursive(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    res = []
    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return res

#Iterative Solution:
def inorderTraversalIterative(self, root):
    res = []
    stack = []

    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
