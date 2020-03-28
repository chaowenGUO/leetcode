/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const dictionary = new Map
    for (const [index, num] of nums.entries())
        if (dictionary.has(num)) return [index, dictionary.get(num)]
        else dictionary.set(target - num, index)
};
