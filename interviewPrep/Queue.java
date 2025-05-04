package interviewPrep;

public class Queue {
    Node left;
    Node right;
    
    public class Node {
        int val;
        Node next;

        public Node(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public Queue() {
        this.left = null;
        this.right = null;
    }

    public void enqueue(int val) {
        Node newNode = new Node(val);
        
        //check if queue is empty
        if(this.left != null) {
            this.right.next = newNode;
            this.right = this.right.next;
        } else {
            this.left = newNode;
            this.right = newNode;
        }
    }

    public int dequeue() {
        if(this.left == null) return -1;

        int val = this.left.val;
        this.left = this.left.next;
        if(this.left == null) {
            this.right = null;
        }

        return val;
    }

}
