/**
 * @param {number[]} nums
 * @return {number}
 */

const lodash = require('lodash')

var findMin = function(nums) {
    return nums[lodash.sortedIndexBy(nums, nums[nums.length - 1], _ => -_)]
};
