package main

//https://leetcode.com/problems/remove-element/submissions/1357142154/

//This soultion uses two pointers left and right and moves them until they are equal
func removeElement1(nums []int, val int) int {
	left, right := 0, len(nums)-1

	//keep looping if left is smaller or equal to right
	for left <= right {
		if nums[left] == val {
			//if left is equal to val, swap value at left with value at right
			nums[left], nums[right] = nums[right], nums[left]
			//move right towards left
			right--
		} else {
			//if value at left is not same as val then move left towards right
			left++
		}
	}
	return left
}

//This soultion uses two pointers but they both start at 0
//Note that in this soultion there would be repeatedn assignments of values at i to k if the value at i is same as val even if i and k are same indexes
func removeElement2(nums []int, val int) int {
	i, k := 0, 0

	for i < len(nums) {
		if nums[i] != val {
			//if vaue at i is not val assign value at i to position k
			nums[k] = nums[i]
			//increment k
			k++
		} else {
			//else assign value at position i to position k without incrementing k
			nums[k] = nums[i]
		}
		i++
	}
	return k
}
