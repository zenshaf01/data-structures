package leetcode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class ReverseLinkedList {
    public static class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    /**
     * Iterative approach is done with 2 pointers
     * Algorithm:
     * 1. initialize 2 pointers curr as head and prev as null
     * 2. start iterating until the curr is null
     * 3. Save curr's next in a temp var
     * 4. Assign prev to curr's next
     * 5. Move prev to curr. prev gets the value of curr. Move prev ahead
     * 6. Assign temp to curr. Move curr ahead
     *
     * Time comlexity: O(n) Linear
     * Space complexity: O(1) list is being reversed in place
     * @param head ListNode
     * @return new Head
     */
    public ListNode reverseListIteratively(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;

        while(curr != null) {
            //Save the next as temp
            ListNode temp = curr.next;
            // assign current's next as it previous
            curr.next = prev;
            // shift pointers forward
            prev = curr;
            curr = temp;
        }
        // return prev which is the new head
        return prev;
    }

    /**
     * This is recursive in nature
     * Algorithm:
     *
     * 1. Keep recursively calling the function if there is a next
     * 2. When you reach base case, keep popping back up and assign the current head to the heads next next.
     * 3. keep returning the newHead which is the last element of the list.
     * @param head ListNode
     * @return ListNode
     */
    public ListNode reverseListRecursively(ListNode head) {
        if(head == null) {
            return null;
        }

        ListNode newHead = head;
        if(head.next != null) {
            newHead = reverseListRecursively(head.next);
            head.next.next = head;
        }
        head.next = null;
        return newHead;
    }
}