package main

//https://leetcode.com/problems/min-stack/description/
type MinStack struct {
	Stack []int
	Mins  []int
}

func Constructor() MinStack {
	return MinStack{
		Stack: []int{},
		Mins:  []int{},
	}
}

func (this *MinStack) Push(val int) {
	this.Stack = append(this.Stack, val)
	minsLength := len(this.Mins)

	if minsLength > 0 {
		minTop := this.Mins[minsLength-1]
		if val < minTop {
			this.Mins = append(this.Mins, val)
		} else {
			this.Mins = append(this.Mins, minTop)
		}
	} else {
		this.Mins = append(this.Mins, val)
	}
}

func (this *MinStack) Pop() {
	length := len(this.Stack)
	minslength := len(this.Mins)

	if length > 0 {
		this.Stack = this.Stack[:length-1]
	}

	if minslength > 0 {
		this.Mins = this.Mins[:minslength-1]
	}
}

func (this *MinStack) Top() int {
	length := len(this.Stack)
	if length > 0 {
		return this.Stack[length-1]
	}
	return 0
}

func (this *MinStack) GetMin() int {
	length := len(this.Mins)
	if length > 0 {
		return this.Mins[length-1]
	}
	return 0
}
