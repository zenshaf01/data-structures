package main

//https://leetcode.com/problems/concatenation-of-array/

//Creates a new array to hold concatenated values. Consumes more memory.
func getConcatenation1(nums []int) []int {
	ans := []int{}

	for range 2 {
		for _, v := range nums {
			ans = append(ans, v)
		}
	}
	return ans
}

//Modifies the input array in place
func getConcatenation2(nums []int) []int {
	length := len(nums)

	for i := 0; i < length; i++ {
		nums = append(nums, nums[i])
	}
	return nums
}
