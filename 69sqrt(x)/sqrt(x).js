/**
 * @param {number} x
 * @return {number}
 */

var mySqrt = function(x) {
    let [left, right] = [0, Math.trunc(x / 2) + 1]
    while (!Object.is(left, right))
    {
        const middle = left + Math.trunc((right - left) / 2)
        if (middle**2 < x) left = middle + 1
        else right = middle
    }
    return Object.is(left**2, x) ? left : left - 1
};
