/**
 * Doubly linked list is a variation of the singly linked list.
 * In addition to the next pointer like the singly linked list, the doubly linked list also has a previous pointer.
 * The doubly linked list also has the head and tail just like the singly linked list
 *
 * Inserting at end O(1): The tail would get the new node as its next and the new node will get the current tail as its previous pointer
 * after which the new node will become the new tail.
 *
 * Removing from end O(1): We will get the node previous from the tail using the tails previous pointer and then set the previous node's next to null,
 * after which we will set the node previous from the current tail as the new tail.
 *
 * Access a random element form the linked list O(n): Find the value you are looking for following the pointers
 *
 * Stack can be implemented with linkedLists but it is best to be done with dynamic arrays since random access in dynamic arrays is in O(1) time.
 */
public class DoublyLinkedList {
    ListNode head;
    ListNode tail;

    public static class ListNode {
        int val;
        ListNode next;
        ListNode prev;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
            this.prev = null;
        }
    }

    public DoublyLinkedList() {
        head = new ListNode(-1);
        tail = new ListNode(-1);

        head.next = tail;
        tail.prev = head;
    }

    public void insertFront(int val) {
        ListNode newNode = new ListNode(val);

        // assign correct pointers for the new node
        newNode.prev = head;
        newNode.next = head.next;

        // update prev pointer for the heads next and the heads next pointer
        head.next.prev = newNode;
        head.next = newNode;
    }

    public void insertEnd(int val) {
        ListNode newNode = new ListNode(val);

        // Update new node pointers
        newNode.next = tail;
        newNode.prev = tail.prev;

        // Update tail pointers
        tail.prev.next = newNode;
        tail.prev = newNode;
    }

    public void removeFront() {
        head.next.next.prev = head;
        head.next = head.next.next;
    }

    public void removeEnd() {
        tail.prev.prev.next = tail;
        tail.prev = tail.prev.prev;
    }

    public void printList() {
        ListNode curr = head.next;
        while(curr != null) {
            System.out.println(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println();
    }
}



