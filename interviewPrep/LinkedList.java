package interviewPrep;

import java.util.*;

public class LinkedList {
    Node head;
    Node tail;

    class Node {
        int val;
        Node next;

        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    public LinkedList() {
        this.head = new Node(-1, null);
        this.tail = head;
    }

    // Add at end O(1)
    public void addAtEnd(int val) {
        Node newNode = new Node(val, null);
        tail.next = newNode;
        tail = tail.next;
    }

    // Add at beginning 
    public void addAtBeginning(int val) {
        Node newNode = new Node(val, null);
        Node temp = head.next;
        newNode.next = temp;
        head.next = newNode;
    }

    // Add at arbitrary position i 
    public void addAtArbitrary(int val, int position) {
        Node newNode = new Node(val, null);
        Node curr = this.head;

        for(int i = 0; i < position; i++) {
            curr = curr.next;
        }

        Node temp = curr.next;
        newNode.next = temp;
        curr.next = newNode;
    }

    // Remove at end
    public void removeAtEnd() {
        tail = tail.next;
    }

    // Remove at beginning
    public void removeAtBeginning() {
        Node temp = head.next.next;
        head.next = temp;
    }

    // Remove at arbitrary
    public void removeAtPosition(int position) {
        int i = 0;
        Node curr = head;

        while(i < position && curr != null) {
            i++;
            curr = curr.next;
        }

        if(curr != null && curr.next != null) {
            if(curr.next == tail) {
                tail = curr;
            }

            curr.next = curr.next.next;
        }
    }

    public void reverse() {
        Node prev = null;
        Node curr = head;

        while(curr != null) {
            Node temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
    }

    public Node merge2SortedLists(Node list1, Node list2) {
        Node result = new Node(0, null);
        Node node = result;

        while(list1 != null && list2 != null) {
            if(list1.val < list2.val) {
                node.next = list1;
                list1 = list1.next;
            } else {
                node.next = list2;
                list2 = list2.next;
            }
            node = node.next;
        }

        if(list1 != null) {
            node.next = list1;
        } else {
            node.next = list2;
        }

        return result.next;
    }


    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        // iterate
        for(int i = 0; i < nums.length; i++) {
            // get complement. This is inverse of saying nums[i] + nums[i+1] = target
            int complement = target - nums[i];
            if(map.containsKey(complement)) {
                return new int[] { i, map.get(complement) };
            }

            map.put(nums[i], i);
        }

        // No solution
        return new int[] {}; 
    }

    public int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            //generate the compliment
            int complement = target - nums[i];
            if(map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }

            map.put(nums[i], i);
        }

        return new int[] {};
    }


    public Node merge2SortedLists2(Node list1, Node list2) {
        Node result = new Node(-1, null);
        Node node = result;

        while(list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                node.next = list1;
                list1 = list1.next;
            } else {
                node.next = list2;
                list2 = list2.next;
            }
            node = node.next;
        }

        if (list1 != null) {
            node.next = list1;
        }

        if(list2 != null) {
            node.next = list2;
        }
        
        return result.next;
    }

    public boolean detectCycle(Node head) {
        if(head == null || head.next == null) {
            return false;
        }

        Node slow = head;
        Node fast = head;

        while(fast != null && slow != null) {
            slow = head.next;
            fast = head.next.next;

            if(slow == fast) {
                return true;
            }
        }

        return false;
    }

    public boolean detectCycle2(Node head) {
        if(head == null || head.next == null) {
            return false;
        }

        Node slow = head;
        Node fast = head;

        while(slow != null && fast != null) {
            slow = slow.next;
            fast = fast.next.next;

            if(slow == fast) {
                return true;
            }
        }

        return false;
    }
}
