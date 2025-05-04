package main

//https://leetcode.com/problems/reverse-linked-list/
type ListNode struct {
	Val  int
	Next *ListNode
}

type SinglyLinkedList struct {
	Head, Tail *ListNode
}

func newSinglyLinkedList() *SinglyLinkedList {
	return &SinglyLinkedList{
		Head: nil,
		Tail: nil,
	}
}

var list = newSinglyLinkedList()

//Iterative solution by using two pointers
//Time complexity: O(n)
//Memory complexity: O(1)
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode = nil
	curr := head

	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}
