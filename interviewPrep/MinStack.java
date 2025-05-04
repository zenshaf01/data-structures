package interviewPrep;

import java.util.Stack;

public class MinStack {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> minStack = new Stack<>();

    public void push(int val) {
        stack.push(val);

        if(minStack.isEmpty() || minStack.peek() >= val) {
            minStack.push(val);
        }
    }

    public void pop() {
        if(stack.isEmpty()) return;

        int top = stack.pop();
        if(top == minStack.peek()) {
            minStack.pop();
        }
    }

    public int getMin() {
        return minStack.peek();
    }
}
