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

const lodash = require('lodash')

var deepestLeavesSum = function(root) {
    let result = []
    let level = [root]
    while (root && level.length)
    {
        result = level.map(node => node.val)
        level = lodash.flatMap(level, node => [node.left, node.right].filter(_ => _))
    }
    return level.reduce((a,b) => a + b)
};
