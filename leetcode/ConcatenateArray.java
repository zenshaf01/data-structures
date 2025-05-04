package leetcode;

public class ConcatenateArray {
    public int[] concatenateArray(int[] nums) {
        int n = nums.length;
        int[] newArray = new int[2 * n];

        for(int i = 0; i < n; i++) {
            newArray[i] = newArray[i + n] = nums[i];
        }
    }
}
