package main

import "fmt"

type Node struct {
	Val  int
	Next *Node
}

func newNode(val int) *Node {
	return &Node{
		Val:  val,
		Next: nil,
	}
}

type SinglyLinkedList struct {
	Head, Tail *Node
}

func newSinglyLinkedList() *SinglyLinkedList {
	node := newNode(-1)
	return &SinglyLinkedList{
		Head: node,
		Tail: node,
	}
}

func (s *SinglyLinkedList) InsertEnd(val int) {
	node := newNode(val)
	//Set tails next as node and then set node as the tail
	s.Tail.Next = node
	s.Tail = node
}

func (s *SinglyLinkedList) Remove(index int) {
	i := 0
	curr := s.Head

	//Find the node previous to the one at index which needs to be deleted
	for i < index && curr != nil {
		i++
		curr = curr.Next
	}

	if curr != nil && curr.Next != nil {
		//if next of current is tail (the one to be deleted) then set curr as tail
		if curr.Next == s.Tail {
			s.Tail = curr
		}

		// set next of current to be next of next
		curr.Next = curr.Next.Next
	}
}

func (s *SinglyLinkedList) Print() {
	curr := s.Head

	for curr != nil {
		fmt.Printf("%d -> ", curr.Val)
		curr = curr.Next
	}

	fmt.Println()
}
