package leetcode;

import java.util.TreeSet;

public class RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
        //Two pointers
        int l = 1;
        for(int r = 1; r < nums.length; r++) {
            if(nums[r] != nums[r - 1]) {
                nums[l++] = nums[r];
            }
        }
        return l;
    }

    public int removeDuplicatesSet(int[] nums) {
        TreeSet<Integer> unique = new TreeSet<>();
        for(int num : nums) {
            unique.add(num);
        }

        int i = 0;
        for(int num : unique) {
            nums[i++] = num;
        }
        return i;
    }
}
