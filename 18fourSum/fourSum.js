/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums.sort((a,b) => a - b)
    const dictionary = new Map()
    for (let left = 0; left < nums.length - 1; ++left)
        for (let right = left + 1; !Object.is(right, nums.length); ++right)
        {
            const total = [left, right].map(_ => nums[_]).reduce((a,b) => a + b)
            dictionary.has(total) ? dictionary.get(total).add([left, right]) : dictionary.set(total, new Set([[left, right]]))
        }
    console.log(dictionary)
    const result = new Set()
    for (let left = 2; left < nums.length - 1; ++left)
        for (let right = left + 1; !Object.is(right, nums.length); ++right)
        {
            const complement = target - [left, right].map(_ => nums[_]).reduce((a,b) => a + b)
            if (dictionary.has(complement)) dictionary.get(complement).forEach(_ => {
                if (_[1] < left) result.add(JSON.stringify([..._, left, right].map(_ => nums[_])))})
        }
    return Array.from(result, JSON.parse)
};
