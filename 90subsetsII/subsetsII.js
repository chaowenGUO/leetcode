/**
 * @param {number[]} nums
 * @return {number[][]}
 */

const lodash = require('lodash')

var subsetsWithDup = function(nums) {
    return nums.sort((a,b) => a - b).reduce((result, num) => [...result, ...result.map(_ => [..._, num]).filter(_ => !result.some($ => lodash.isEqual($, _)))], [[]])
};
