package main

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
func removeDuplicates(nums []int) int {
	length := len(nums)
	if length < 2 {
		return length
	}
	//maintain two pointers. i for traversal and k for the shift
	k, i := 1, 1
	for i < length {
		//if current and previous are not same then shift element at i to k
		if nums[i] != nums[i-1] {
			nums[k] = nums[i]
			//We only increment k if we find a unique element. This helps us maintain a spot on where to put the next unique value
			k++
		}
		i++
	}
	return k
}
