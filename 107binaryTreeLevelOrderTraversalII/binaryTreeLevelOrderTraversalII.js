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

var levelOrderBottom = function(root) {
    const result = []
    let level = [root]
    while (root && level.length)
    {
        result.push(level.map(node => node.val))
        level = level.flatMap(node => [node.left, node.right].filter(_ => _))
    }
    return result.reverse()
};
