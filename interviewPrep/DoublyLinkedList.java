package interviewPrep;

public class DoublyLinkedList {
    public class Node {
        int val;
        Node prev;
        Node next;

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node prev, Node next) {
            this.val = val;
            this.prev = prev;
            this.next = next;
        }
    }

    Node head;
    Node tail;

    public DoublyLinkedList() {
        this.head = new Node(-1);
        this.tail = new Node(-1);
        head.next = tail;
        tail.prev = head;
    }

    public void insertAtEnd(int val) {
        Node newNode = new Node(val);
        newNode.next = tail;
        newNode.prev = tail.prev;

        tail.prev.next = newNode;
        tail.prev = newNode;
    }

    public void insertAtBeginning(int val) {
        Node newNode = new Node(val);
        newNode.prev = head;
        newNode.next = head.next;

        head.next.prev = newNode;
        head.next = newNode;
    }

    public void insertAtPosition(int val, int position) {
        Node curr = this.head;

        for(int i = 0; i < position; i++) {
            curr = curr.next;
        }

        if(curr != null) {
            Node newNode = new Node(val);
            newNode.prev = curr;
            newNode.next = curr.next;
            curr.next.prev = newNode;
            curr.next = newNode;
        }
    }

    public void removeFromEnd() {
        tail.prev.prev.next = tail;
        tail.prev = tail.prev.prev;
    }

    public void removeFront() {
        head.next.next.prev = head;
        head.next = head.next.next;
    }

    public void removeAtPosition(int position) {
        Node curr = this.head;

        for(int i = 0; i < position; i++) {
            curr = curr.next;
        }

        if(curr == tail) {
            removeFromEnd();
        }

        if(curr == head) {
            removeFront();
        } 

        if(curr != null) {
            curr.next = curr.next.next;
            curr.next.prev = curr;
        }
    }

    public Node reverse() {
        Node curr = this.head.next;
        Node temp = null;

        while (curr != null) {
            temp = curr.prev;
            curr.prev = curr.next;
            curr.next = temp;

            curr = curr.prev;
        }

        Node firstReal = tail.prev;
        Node lastReal = head.next;

        head.next = firstReal;
        firstReal.prev = head;

        tail.prev = lastReal;
        lastReal.next = tail;

        return head;
    }

    public Node reverse2() {
        Node curr = this.head.next;
        Node temp = null;

        while(curr != null) {
            temp = curr.prev;
            curr.prev = curr.next;
            curr.next = temp;

            curr = curr.prev;
        }

        Node first = tail.prev;
        Node last = head.next;

        head.next = first;
        first.prev = head;

        tail.prev = last;
        last.next = tail;

        return head;
    }
}
