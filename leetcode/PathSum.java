package leetcode;

class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return this.hasPathSum(root, targetSum, 0);
    }

    public boolean hasPathSum(TreeNode root, int targetSum, int accumulator) {
        if(root == null) return false;

        accumulator += root.val;
        if(root.left == null && root.right == null && accumulator == targetSum) return true;

        if(hasPathSum(root.left, targetSum, accumulator)) return true;
        if(hasPathSum(root.right, targetSum, accumulator)) return true;

        return false;
    }
}
