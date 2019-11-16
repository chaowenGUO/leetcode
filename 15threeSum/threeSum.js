/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const result = []
    nums.sort((a, b) => a - b)
    for (let index = 0; index < nums.length - 2;)
    {
        const num = nums[index]
        if (num > 0) break
        let [left, right] = [index + 1, nums.length - 1]
        while (left < right)
        {
            const [numsLeft, numsRight] = [left, right].map(_ => nums[_])
            const total = num + numsLeft + numsRight
            if (Object.is(total, 0)) result.push([num, numsLeft, numsRight])
            if (total <= 0) while (left < right && Object.is(numsLeft, nums[left])) ++left
            if (total >= 0) while (left < right && Object.is(numsRight, nums[right])) --right
        }
        while (Object.is(num, nums[index]) && index < nums.length - 2) ++index
    }
    return result
};
