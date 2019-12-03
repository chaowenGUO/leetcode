/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a,b) => a - b)
    let result = Array.from({length:3}, (_, index) => nums[index]).reduce((a,b) => a + b)
    for (let index = 0; index != nums.length - 2;)
    {
        const num = nums[index]
        let [left, right] = [index + 1, nums.length - 1]
        while (!Object.is(left, right))
        {
            const [numsLeft, numsRight] = [left, right].map(_ => nums[_])
            const total = num + numsLeft + numsRight
            if (Object.is(total, target)) return target
            if (total <= target) while (!Object.is(left, right) && Object.is(numsLeft, nums[left])) ++left
            if (total >= target) while (!Object.is(left, right) && Object.is(numsRight, nums[right])) --right
            if (Math.abs(total - target) < Math.abs(result - target)) result = total
        }
        while (Object.is(nums[index], num) && index != nums.length - 2) ++index
    }
    return result
};
