/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    return nums.reduce((result, num) => [...result, ...result.map(_ => [..._, num])], [[]])
};
