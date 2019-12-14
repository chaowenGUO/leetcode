/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let [left, right] = [0, height.length - 1]
    let result = 0
    while (!Object.is(left, right))
    {
        result = Math.max(result, (right - left) * Math.min(...[left, right].map(_ => height[_])));
        [left, right].map(_ => height[_]).reduce((a,b) => a - b) < 0 ? ++left : --right
    }
    return result
};
