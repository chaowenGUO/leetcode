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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        final var result = new ArrayList<List<Integer>>();
        var level = Arrays.asList(root);
        var direction = true;
        while (Objects.nonNull(root) && !level.isEmpty())
        {
            final var val = level.stream().map(node -> node.val).collect(Collectors.toList());
            if (!direction) Collections.reverse(val);
            direction = !direction;
            result.add(val);
            level = level.stream().flatMap(node -> Stream.of(node.left, node.right)).filter(Objects::nonNull).collect(Collectors.toList());
        }
        return result;
    }
}
