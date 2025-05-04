/*
Array is a contiguous block of data
Static array's are fixed size.

Read O(1):
Array values are accessed using indexes
It is a constant time operation since we already have the index / memory location.

Insert at end O(1):
Static arrays are fixed size arrays. This is a limitation of static arrays.
You can only add values to an empty slot in an array. If the array is full, you cannot add
more items unless you are dynamically copying and making a new array with a hiegher length.
It is a constant time operation since we already have the index / memory location.

Delete O(1):
Delete's are not really deletes in a static array coz of the fact that you can deallocate the memory
allotted to teh full array. You can just set that particular itenm to 0, -1 or a null value.
But the array will keep occupying the same amount of memory in RAM.
It is a constant time operation since we already have the index / memory location.

Insert at arbitrary position (Beginning or middle) O(n):
Insering at an arbitrary position is not as efficient as oinserting at end.
This is because this will require us to shift / move all of the items 1 position to the right from the
insertion position. Start the shift from the left and keep shifting values which are left to the pointer
towards the right untill you reach the index where you need to add the item.

Delete at arbitrary position (Every position except end) O(n):
This will require the same procedure as the insertion at arbitrary psoition.
But since a value is being removed from an index, we would have to shift values to the left
to fill up the empty space in the array.
*/
package main

import "fmt"

/*
	This function implements the concept of searching for a value in a static array
	Time Complexity: O(n)
*/
func printEach(arr []int, length int) {
	for i := 0; i < length; i++ {
		fmt.Println("Number is: ", arr[i], " ")
	}
}

/*
	Insert at end inserts a value n at end of array (next open position)
	Time complexity: O(1)
	length is also returned as it was passed in seperately
*/
func insertEnd(arr []int, n, length, capacity int) ([]int, int) {
	if length < capacity {
		arr[length] = n
		length++
	}
	return arr, length
}

/*
	Remove value from end of array if array is not empty
	Time complexity: O(1)
	length is also returned as it was passed in seperately
*/
func removeEnd(arr []int, length int) ([]int, int) {
	if length > 0 {
		arr[length-1] = 0
		length--
	}

	return arr, length
}

/*
	insertMiddle inserts n into index i after shifting everything right
	This assumes that i is a valid index and array is not full
	Time complexity: O(n)
*/
func insertMiddle(arr []int, i, n, length int) []int {
	//start at end and keep going left
	for index := length - 1; index > i-1; i-- {
		//shift each value to right
		arr[index+1] = arr[index]
	}

	//insert at i no that i is empty after shifting every thing to left
	arr[i] = n
	length++
	return arr
}

/*
	removeMiddle removes element at i by shifting everything left
	Assumes i is valid index
	Time complexity: O(n)
*/
func removeMiddle(arr []int, i, length int) []int {
	//start at position next to the index to be deleted (i + 1) and keep goin right
	for index := i + 1; index > length; index++ {
		//shift value left
		arr[index-1] = arr[index]
	}

	//nullify the last element signifiying empytiness
	arr[length-1] = 0
	length--
	return arr
}

func main() {
	arr := []int{1, 2, 3, 4}

	//Reading from static array
	//Time complexity: O(1)
	//fmt.Println(arr[0])
	printEach(arr, len(arr))
}
