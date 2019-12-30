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
    public int deepestLeavesSum(TreeNode root) {
        List<Integer> result = null;
        List<TreeNode> level = Arrays.asList(root);
        while (root != null && !level.isEmpty())
        {
            result = level.stream().map(node -> node.val).collect(Collectors.toList());
            level = level.stream().flatMap(node -> Stream.of(node.left, node.right).filter($ -> $ != null)).collect(Collectors.toList());
        }
        return result.stream().mapToInt(Integer::intValue).sum();
    }
}
