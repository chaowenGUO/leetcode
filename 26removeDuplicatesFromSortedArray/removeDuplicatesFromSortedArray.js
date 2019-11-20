/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let index = nums.length ? 1 : 0
    nums.forEach((num, _, array) => {
        if (num > array[index - 1])
        {
            array[index] = num
            ++index
        }})
    return index
};
