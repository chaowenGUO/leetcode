/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

const lodash = require('lodash')

var threeSumClosest = function(nums, target) {
    nums.sort(lodash.subtract)
    let result = lodash.chain(nums).slice(0, 3).sum()
    for (let index = 0; !Object.is(index, nums.length - 2);)
    {
        const num = nums[index]
        let left = index + 1, right = nums.length - 1
        while (!Object.is(left, right))
        {
            const numsLeft = nums[left], numsRight = nums[right]
            const total = num + numsLeft + numsRight
            if (Object.is(total, target)) return target
            if (total <= target) while (!Object.is(left, right) && Object.is(numsLeft, nums[left])) ++left
            if (total >= target) while (!Object.is(left, right) && Object.is(numsRight, nums[right])) --right
            if (Math.abs(total - target) < Math.abs(result - target)) result = total
        }
        while (!Object.is(index, nums.length - 2) && Object.is(nums[index], num)) ++index
    }
    return result
};
