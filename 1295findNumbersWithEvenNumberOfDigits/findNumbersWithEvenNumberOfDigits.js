/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    return nums.map(num => 1 - num.toString().length & 1).filter(Object.is.bind(null, 1)).length
};
