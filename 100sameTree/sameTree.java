/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p != null && q != null) return p.val == q.val && this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
        else return p == q;
    }
}
