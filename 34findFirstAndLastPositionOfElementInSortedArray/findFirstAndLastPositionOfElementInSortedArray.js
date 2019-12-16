/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const lodash = require('lodash')

var searchRange = function(nums, target) {
    const [left, right] = [lodash.sortedIndex, lodash.sortedLastIndex].map(_ => _(nums, target))
    return !Object.is(left, right) ? [left, right - 1] : Array(2).fill(-1)
}; 
