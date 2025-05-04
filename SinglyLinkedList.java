/**
 * Linked lists are made up of list nodes or nodes
 * A list nodes has a value (can bee another object, integer, string or anything) and a next pointer to the next node in the list
 * A linked list is dynamic and can infinitely grow
 * A linked list does not have index based access because we don't know where the next node would be in memory.
 * We have memory addressed which can be used to access the next node.
 * The next pointer can be null denoting that the linked list has only 1 node
 * Linked lists have a head and a tail nodes
 *
 * Insert at end O(1) if at end but O(n) if in middle: set the new node to tail.next and then set new node to be the new tail.
 * Remove O(1) if at beginning but O(n) if at middle: set the previous node next to be the next next of the same node.
 */
public class SinglyLinkedList {
    ListNode head;
    ListNode tail;

    public class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public SinglyLinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    // O(1)
    public void insertEnd(int val) {
        tail.next = new ListNode(val);
        tail = tail.next;
    }

    //O(n)
    public void remove(int index) {
        int i = 0;
        ListNode curr = head;

        // Get the node just before the node to be removed
        while(i < index && curr.next != null) {
            i++;
            curr = curr.next;
        }

        //remove the node ahead of curr
        if(curr != null && curr.next != null) {
            // if the next is tail, then the current becomes the new tail
            if(curr.next == tail) {
                tail = curr;
            }

            //the next becomes the node at next of next. If the next was tail this means it would now be null
            curr.next = curr.next.next;
        }
    }

    public void print() {
        // This is because we have initialised head as a -1
        ListNode curr = head.next;
        while(curr != null) {
            System.out.println(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println();
    }
}
