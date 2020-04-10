/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (!root) return 0
    else
    {
        const depth = [root.left, root.right].map(minDepth)
        return 1 + (Math.min(...depth) || Math.max(...depth))
    }
};
