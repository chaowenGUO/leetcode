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
    public int minDepth(TreeNode root) {
        if (Objects.isNull(root)) return 0;
        else
        {
            final var depth = Stream.of(root.left, root.right).map(this::minDepth).collect(Collectors.toList());
            final var min = Collections.min(depth);
            return 1 + (min != 0 ? min : Collections.max(depth));
        }
    }
}
