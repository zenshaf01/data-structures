package main

// Insertion and deltion can be done in O(1). This means that you can make stacks using a doubly linked lists. It is uncommon but can be done.
// Remember stacks follow LIFO rule
// Linked lists lose to dynamic arrays where random access is required.

// Access: O(n)
// Insertion / Delete at end: O(1)
// Insertion / Delete at middle: O(1) -> this is only if you have access to the element being deleted. Otherwise O(n) will be required to find the element to be deleted.

type DoublylinkedListNode struct {
	Val      int
	Next     *DoublylinkedListNode
	Previous *DoublylinkedListNode
}

func newDoublyNode(val int, prev, next *DoublylinkedListNode) *DoublylinkedListNode {
	return &DoublylinkedListNode{
		Val:      val,
		Next:     next,
		Previous: prev,
	}
}

type DoublyLinkedList struct {
	Head, Tail *DoublylinkedListNode
}

func newDoublyLinkedList() *DoublyLinkedList {
	head := newDoublyNode(-1, nil, nil)  //dummy head node
	tail := newDoublyNode(-1, head, nil) //dummy tail node

	head.Next = tail

	return &DoublyLinkedList{
		Head: head,
		Tail: tail,
	}
}

func (this *DoublyLinkedList) Get(index int) int {
	curr := this.Head.Next

	// keep moving current to left while decrementing the index to find the correct node
	for curr != nil && index > 0 {
		curr = curr.Next
		index--
	}

	if curr != nil && curr != this.Tail && index == 0 {
		return curr.Val
	}

	return -1
}

func (this *DoublyLinkedList) AddAtHead(val int) {
	node := newDoublyNode(val, this.Head, this.Head.Next)
	this.Head.Next.Previous = node
	this.Head.Next = node
}

func (this *DoublyLinkedList) AddAtTail(val int) {
	node := newDoublyNode(val, this.Tail.Previous, this.Tail)
	this.Tail.Previous.Next = node
	this.Tail.Previous = node
}

func (this *DoublyLinkedList) AddAtIndex(val, index int) {
	curr := this.Head.Next

	for curr.Next != nil && index > 0 {
		curr = curr.Next
		index--
	}

	if index == 0 {
		node := newDoublyNode(val, curr.Previous, curr)
		curr.Previous.Next = node
		curr.Previous = node
	}

	return
}

func (this *DoublyLinkedList) DeleteAtIndex(val, index int) {
	curr := this.Head.Next

	for curr.Next != nil && index > 0 {
		curr = curr.Next
		index--
	}

	if index == 0 && curr != nil && curr != this.Tail {
		prev, next := curr.Previous, curr.Next
		prev.Next = next
		next.Previous = prev
	}
	return
}
