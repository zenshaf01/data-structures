public class Sorting {

    public void insertionSort(int[] nums) {
        // Single element list is already sorted
        if(nums.length == 1) {
            return;
        }

        // Start the outer loop at 1
        for(int i = 1; i < nums.length; i++) {
            // start pointer for inner loop j at 1 position behind i
            int j = i - 1;

            // while j (left) is in bound and it is larger than i (right)
            while(j >= 0 && nums[j + 1] < nums[j]) {
                // perform the swap
                int temp = nums[j + 1];
                nums[j + 1] = nums[j];
                nums[j] = temp;
                j--;
            }
        }
    }

    public void mergeSort() {

    }
}
