/**
 * @param {number[]} nums
 * @return {number}
 */
function even(num)
{
    let result = 0
    while (num)
    {
        num = Math.trunc(num / 10)
        ++result
    }
    return 1 - result & 1
}

var findNumbers = function(nums) {
    return nums.map(even).reduce((a,b) => a + b)
};
