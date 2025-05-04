package main

type Stack struct {
	Stack  []int
	Length int
}

func (s *Stack) Push(val int) {
	s.Stack = append(s.Stack, val)
	s.Length++
}

func (s *Stack) Pop() int {
	if s.Length == 0 {
		return 0
	}
	res := s.Stack[s.Length-1]
	s.Stack = s.Stack[:s.Length-1]
	s.Length--
	return res
}

func (s *Stack) Peek() int {
	return s.Stack[s.Length-1]
}
