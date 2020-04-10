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
    public int maxDepth(TreeNode root) {
        return Objects.nonNull(root) ? Stream.of(root.left, root.right).mapToInt(this::maxDepth).max().orElse(0) + 1 : 0;
    }
}
