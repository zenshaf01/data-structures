# subOptimal
def kth_smallest_sub_optimal_recursive(root, k):
    arr = []
    def dfs(root):
        if not root:
            return None
        dfs(root.left)
        arr.append(root.val)
        dfs(root.right)
    dfs(root)
    return arr[k-1]


def kth_smallest_iterative(root, k):
    # maintain a stack
    stack = []
    curr = root

    # keep iterating while curr is non null or there is something in the stack
    while curr or stack:
        while curr:
            # visit the current node and put it in the stack
            stack.append(curr)
            # go down the left subtree
            curr = curr.left

        # when you have reached the smallest node on the left side. pop from the stack and set it to current
        curr = stack.pop()
        # decrement k
        k -= 1

        # if k is 0, it means we have reached the desired node at which the value is 
        if k == 0: 
            return curr.val
        
        # if k is still not 0 then set curr to right to traverse the right side and try to find the kth smallest
        curr = curr.right