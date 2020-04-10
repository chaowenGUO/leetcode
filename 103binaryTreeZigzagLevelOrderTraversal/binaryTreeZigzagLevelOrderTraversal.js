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

Array.prototype.flatMap = function(callBack)
{
    return lodash.flatMap(this, callBack)
}

var zigzagLevelOrder = function(root) {
    const result = []
    let level = [root], direction = true
    while (root && level.length)
    {
        const val = level.map(node => node.val)
        result.push(direction ? val : val.reverse())
        direction = !direction
        level = level.flatMap(node => [node.left, node.right].filter(_ => _))
    }
    return result
};
