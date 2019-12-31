/**
 * @param {number[]} nums
 * @return {number[][]}
 */

const lodash = require('lodash')

var subsetsWithDup = function(nums) {
    return nums.sort((a,b) => a - b).reduce((result, num) => lodash.uniqWith([...result, ...result.map(_ => [..._, num])], lodash.isEqual), [[]])
};
