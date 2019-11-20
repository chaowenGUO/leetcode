/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    for (let index = 0; !Object.is(nums.length, index); ++index)
        while (0 <= nums[index] - 1 && nums[index] - 1 < nums.length && !Object.is(nums[nums[index] - 1], nums[index])) [nums[nums[index] - 1], nums[index]] = [nums[index], nums[nums[index] - 1]]
    for (let index = 0; !Object.is(nums.length, index); ++index)
        if (!Object.is(nums[index], index + 1)) return index + 1
    return nums.length + 1
};
