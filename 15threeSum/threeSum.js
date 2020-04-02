/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b) => a - b)
    const result = []
    for (let index = 0; index < nums.length - 2;)
    {
        const num = nums[index]
        if (num > 0) break
        let left = index + 1, right = nums.length - 1
        while (!Object.is(left, right))
        {
            const numsLeft = nums[left], numsRight = nums[right]
            const total = num + numsLeft + numsRight
            if (Object.is(total, 0)) result.push([num, numsLeft, numsRight])
            if (total <= 0) while (!Object.is(left, right) && Object.is(numsLeft, nums[left])) ++left
            if (total >= 0) while (!Object.is(left, right) && Object.is(numsRight, nums[right])) --right
        }
        while (index < nums.length - 2 && Object.is(nums[index], num)) ++index
    }
    return result
};
