package interviewPrep;

public class BrowserHistory {
    Node curr;

    //Define the node class
    public class Node {
        String val;
        Node prev;
        Node next;

        public Node(String val, Node prev, Node next) {
            this.val = val;
            this.prev = prev;
            this.next = next;
        }

        public Node(String val) {
            this.val = val;
            this.prev = null;
            this.next = null;
        }
    }


    public BrowserHistory(String val) {
        this.curr = new Node(val);
    }

    public void visit(String url) {
        // create the new node
        Node newPage = new Node(url, this.curr, null);

        // link curr and new node
        this.curr.next = newPage;
        // move curr to next / new page
        this.curr = this.curr.next;
    }

    public String back(int steps) {
        // keep gong back till you there is a curr and the steps is non zero
        while (this.curr.prev != null && steps > 0) {
            this.curr = this.curr.prev;
            steps--;
        }

        return this.curr.val; 
    }

    public String forward(int steps) {
        while (this.curr.next != null && steps > 0) {
            this.curr = this.curr.next;
            steps--;
        }

        return this.curr.val;
    }
}
