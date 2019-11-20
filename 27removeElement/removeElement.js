/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let index = 0
    nums.forEach((num, $, array) => {
        if (!Object.is(num, val))
        {
            array[index] = num
            ++index}})
    return index
};
