/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */

const lodash = require('lodash')

var zigzagLevelOrder = function(root) {
    const result = []
    let level = [root]
    while (root && level.length)
    {
        result.push(level.map(node => node.val))
        level = lodash.flatMap(level, node => [node.left, node.right]).filter(_ => _)
    }
    let direction = true
    for (let level of result)
    {
        level = direction ? level : level.reverse()
        direction = !direction
    }
    return result
};
