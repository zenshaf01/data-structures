'''
Link: https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Solution:
This can be solved with backtracking.
Trick: The trick is to make a decision on each element of the input array on whether to add it or not.
'''
def subsets(nums):
    res = []
    subsets = []

    def dfs(i):
        if i >= len(nums):
            res.append(subsets.copy())
            return
        
        subsets.append(nums[i])
        # left branch - the decision of when we add the element at i to the subset
        dfs(i + 1)
        # right branch - the decsion of when we dont add the element at i to the subset
        subsets.pop()
        dfs(i + 1)

    dfs(0)
    return res
         
