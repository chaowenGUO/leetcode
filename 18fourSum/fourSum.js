/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */

const lodash = require('lodash')

var fourSum = function(nums, target) {
    nums.sort((a,b) => a - b)
    const dictionary = lodash.groupBy(lodash.flatMap(lodash.range(nums.length - 1), left => lodash.range(left + 1, nums.length).map(right => [left, right])), _ => _.map(_ => nums[_]).reduce((a,b) => a + b))    
    const result = new Set()
    for (let left = 2; left < nums.length - 1; ++left)
        for (let right = left + 1; !Object.is(right, nums.length); ++right)
        {
            const complement = target - [left, right].map(_ => nums[_]).reduce((a,b) => a + b)
            if (complement in dictionary) dictionary[complement].forEach(_ => {
                if (_[1] < left) result.add(JSON.stringify([..._, left, right].map(_ => nums[_])))})
        }
    return Array.from(result, JSON.parse)
};
