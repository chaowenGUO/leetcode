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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        final var result = new ArrayList<List<Integer>>();
        var level = Arrays.asList(root);
        while (Objects.nonNull(root) && !level.isEmpty())
        {
            result.add(level.stream().map(node -> node.val).collect(Collectors.toList()));
            level = level.stream().flatMap(node -> Stream.of(node.left, node.right).filter(Objects::nonNull)).collect(Collectors.toList());
        }
        Collections.reverse(result);
        return result;
    } 
}
