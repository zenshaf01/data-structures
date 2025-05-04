package interviewPrep;

import java.util.Queue;
import java.util.LinkedList;

public class BST {
    public class Node {
        int val;
        Node left;
        Node right;

        public Node(int val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }

    public Node insert(Node root, int val) {
        if(root == null) {
            return new Node(val);
        }
        if(val > root.val) {
            root.right = insert(root.right, val);
        } else if(val < root.val) {
            root.left = insert(root.left, val);
        }
        return root;
    }

    public Node findMin(Node root) {
        Node curr = root;
        while(curr != null && curr.left != null) {
            curr = curr.left;
        }
        return curr;
    }

    public boolean binarySearchOnBST(Node root, int target) {
        if(root == null) {
            return false;
        }

        if(target < root.val) {
            return binarySearchOnBST(root.left, target);
        } else if(target > root.val) {
            return binarySearchOnBST(root.right, target);
        } else {
            return true;
        }
    }

    public Node remove(Node root, int target) {
        if(root == null) {
            return null;
        }

        if(target < root.val) {
            root.left = remove(root.left, target);
        } else if(target > root.val) {
            root.left = remove(root.right, target);
        } else {
            if(root.left == null) {
                return root.right;
            } else if(root.right == null) {
                return root.left;
            } else {
                Node minNode = findMin(root.right);
                root.val = minNode.val;

                root.right = remove(root.right, minNode.val);
            }
        }

        return root;
    }

    public void inorderDFS(Node root) {
        if(root == null) return;

        inorderDFS(root.left);
        System.err.println("Val: " + root.val);
        inorderDFS(root.right);
    }

    public void preorderDFS(Node root) {
        if(root == null) return;

        System.err.println("Val: " + root.val);
        preorderDFS(root.left);
        preorderDFS(root.right);
    }

    public void postOrderDFS(Node root) {
        if(root == null) return;

        postOrderDFS(root.left);
        postOrderDFS(root.right);
        System.err.println("Val: " + root.val);
    }
        Queue<Node> tree = new LinkedList<>();

    public int levelOrderTraversal(Node root) {
        Queue<Node> queue = new LinkedList<>();

        if(root != null) {
            queue.add(root);
        }

        int level = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();

            for(int i = 0; i < size; i++) {
                Node curr = queue.poll();
                System.out.println("Val: " + curr.val);

                if(curr.left != null) {
                    queue.add(curr.left);
                } else if(curr.right != null) {
                    queue.add(curr.right);
                }
            }
            level++;
        }
        return level;
    }

    public int levelOrderTraversal2(Node root) {
        Queue<Node> queue = new LinkedList<>();
        int level = 0;

        if(root == null) return level;
        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node node = queue.poll();
                System.out.println("Val: " + node.val);

                if (node.left != null) {
                    queue.add(node.left);
                } else if(node.right != null) {
                    queue.add(node.right);
                }
            }
            level++;
        }
        return level;
    }
}
