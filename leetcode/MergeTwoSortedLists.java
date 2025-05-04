package leetcode;

public class MergeTwoSortedLists {

    public static class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Start with a dummy node to avoid null edge case
        ListNode dummy = new ListNode(0);
        ListNode result = dummy;

        // keep iterating until at least 1 node becomes null
        while(list1 != null && list2 != null) {
            if(list1.val < list2.val) {
                result.next = list1;
                list1 = list1.next;
            } else {
                result.next = list2;
                list2 = list2.next;
            }

            result = result.next;
        }

        if(list1 != null) {
            result.next = list1;
        } else {
            result.next = list2;
        }

        return dummy.next;
    }
}
