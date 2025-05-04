/**
 * Queue's are another data structure that support the FIFO (First in First out) rule.
 * Elements are removed in the same order as they were added.
 *
 * Operations:
 * Enqueue O(1): Elements are pushed to the end of the queue.
 * Dequeue O(1): Elements are remove from the beginning.
 */
public class Queue {
     public class ListNode {
         int val;
         ListNode next;

         public ListNode(int val) {
             this.val = val;
             this.next = null;
         }
    }

    ListNode left;
    ListNode right;

    public Queue() {
        left = null;
        right = null;
    }

    public void enqueue(int val) {
        ListNode newNode = new ListNode(val);

        // check if there is a right, this would mean that the list is not empty
        if(right != null) {
            right.next = newNode;
            right = right.next;
        } else {
            // set left and right to same node since this node is the first one in the list
            left = newNode;
            right = newNode;
        }
    }

    public int dequeue() {
        // Check if the queue is empty
        if(left == null) {
            System.exit(0);
        }

        int val = left.val;
        left = left.next;
        if(left == null) {
            right = null;
        }
        return val;
    }

}
