package main

import "fmt"

type DynamicArray struct {
	Capacity int
	Length   int
	Arr      []int
}

func NewDynamicArray() *DynamicArray {
	return &DynamicArray{
		Capacity: 2,
		Length:   0,
		Arr:      make([]int, 2),
	}
}

func (d *DynamicArray) push(n int) {
	//If length has reached capacity then resize
	if d.Length == d.Capacity {
		d.resize()
	}

	//Push to end
	d.Arr[d.Length] = n
	d.Length++
}

func (d *DynamicArray) resize() {
	d.Capacity = d.Capacity * 2
	newArr := make([]int, d.Capacity)

	//can also use copy(newArr, d.Arr)
	for i := 0; i < len(d.Arr); i++ {
		newArr[i] = d.Arr[i]
	}

	d.Arr = newArr
}

func (d *DynamicArray) pop() {
	if d.Length > 0 {
		d.Arr[d.Length] = 0
		d.Length--
	}
}

func (d *DynamicArray) Get(i int) int {
	if i < d.Length {
		return d.Arr[i]
	}
	return -1
}

func (d *DynamicArray) Insert(i, val int) {
	if i < d.Length {
		d.Arr[i] = val
	}
}

func (d *DynamicArray) Print() {
	for i := 0; i < d.Length; i++ {
		fmt.Println(d.Arr[i])
	}
}
