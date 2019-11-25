/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let index = 0
    nums.forEach((num, _, array) => {
        if (index < 2 || num > array[index - 2])
        {
            array[index] = num
            ++index
        }})
    return index
};
