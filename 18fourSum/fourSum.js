/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */

const lodash = require('lodash')

var fourSum = function(nums, target) {
    nums.sort((a,b) => a - b)
    const dictionary = lodash.groupBy(lodash.flatten(Array.from({length: nums.length - 1}, (_, left) => lodash.range(left + 1, nums.length).map(right => [left, right]))), _ => _.map(_ => nums[_]).reduce((a,b) => a + b))
    return lodash.uniqWith(lodash.flatMap(Object.entries(lodash.groupBy(lodash.flatMap(lodash.range(2, nums.length - 1), left => lodash.range(left + 1, nums.length).map(right => [left, right])), _ => target - _.map(_ => nums[_]).reduce((a,b) => a + b))), ([key, value]) => lodash.flatMap(dictionary[key] || [], x => value.map(y => [...x, ...y])).filter(_ => _[1] < _[2]).map(_ => _.map(_ => nums[_]))), lodash.isEqual)
};
