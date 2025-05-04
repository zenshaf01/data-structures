package interviewPrep;
import java.util.ArrayList;
import java.util.Stack;


public class CustomStack {
    ArrayList<Integer> stack = new ArrayList<>();

    public CustomStack() {}

    public void push(int val) {
        this.stack.add(val);
    }

    public void pop() {
        if(stack.isEmpty()) return;

        this.stack.remove(stack.size() -1);
    } 

    public void peek() {
        if(stack.isEmpty()) return;
        this.stack.get(stack.size() - 1);
    }

    public int size() {
        return stack.size();
    }

    public void resetStack() {
        this.stack = new ArrayList<>();
    }

    public boolean isValidParenthesis(String s) {
        Stack<Character> cStack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(c == '(') cStack.add(')');
            else if(c == '{') cStack.add('}');
            else if(c == '[') cStack.add(']');
            else if(cStack.isEmpty() || cStack.pop() != c) {
                return false;
            }
        }
        return cStack.isEmpty();
    }


    public boolean isValidParenthesis2(String word) {
        Stack<Character> stack = new Stack<>();

        for(char c : word.toCharArray()) {
            if(c == '(') stack.add(')');
            else if(c == '{') stack.add('}');
            else if(c == '[') stack.add(']');
            else if(stack.isEmpty() || stack.pop() != c) {
                return false;
            } 
        }

        return stack.isEmpty();
    }
}
