package main

//https://leetcode.com/problems/valid-parentheses/
//Time complexity: O(n) -> iterating over n characters.
//Space complexity: O(n) -> stack grows with n.

//uses map
func isValid1(s string) bool {
	pairs := map[byte]byte{
		'}': '{',
		']': '[',
		')': '(',
	}

	stack := make([]byte, 0)

	for _, char := range []byte(s) {
		pair, ok := pairs[char]
		if !ok {
			stack = append(stack, char)
			continue
		}

		if len(stack) == 0 {
			return false
		}

		if stack[len(stack)-1] != pair {
			return false
		}

		stack = stack[:len(stack)-1]
	}

	return len(stack) == 0
}

//only uses stack
func isValid2(s string) bool {
	stack := []string{}
	for _, c := range s {
		str := string(c)
		left := isLeft(str)
		if left {
			stack = append(stack, str)
		} else {
			if len(stack) > 0 {
				popped := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				right := getRight(popped)
				if right == "unknown parentheses." {
					return false
				}

				if right == str {
					continue
				} else {
					return false
				}
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

func isLeft(str string) bool {
	switch str {
	case "(":
		return true
	case "[":
		return true
	case "{":
		return true
	default:
		return false
	}
}

func getRight(str string) string {
	switch str {
	case "{":
		return "}"
	case "(":
		return ")"
	case "[":
		return "]"
	default:
		return "unknown parentheses."
	}
}
