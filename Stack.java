import java.util.ArrayList;
import java.util.List;

public class Stack {
    /**
     * The stack data structure is a LIFO (Last In First Out Data structure)
     * Think of stack being a stack of plates
     * You can only add or remove elements from the top of the stack
     * Top of the stack means the last element added
     * Stacks can grow infinitely as they are implemented using a dynamic array
     * Stack supports 3 operations:
     * Push O(1)
     * Pop O(1)
     * Peek (Top) O(1)
     *
     * Example uses:
     * Can be used to reverse a sequence.
     */

    List<Integer> stack = new ArrayList<>();

    public Stack() {}

    public void push(int val) {
        this.stack.add(val);
    }

    public void pop() {
        if(stack.isEmpty()) return;

        this.stack.remove(stack.size() - 1);
    }

    public int peek() {
        return this.stack.get(stack.size() - 1);
    }

    public int size() {
        return stack.size();
    }


}
