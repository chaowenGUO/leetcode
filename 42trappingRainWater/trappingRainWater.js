/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let [result, level] = Array(2).fill(0)
    let [left, right] = [0, height.length - 1]
    while (left < right)
    {
        const low = Math.min(...[left, right].map(_ => height[_]));
        [left, right].map(_ => height[_]).reduce((a, b) => a - b) < 0 ? ++left : --right
        level = Math.max(level, low)
        result += level - low
    }
    return result
};
