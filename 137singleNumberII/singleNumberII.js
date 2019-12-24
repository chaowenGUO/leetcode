/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let [a, b] = Array(2).fill(0)
    nums.forEach(num => {
        b = (b ^ num) & ~a
        a = (a ^ num) & ~b})
    return b
};
