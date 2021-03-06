/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || !(x % 10) && x) return false
    else
    {
        let result = 0
        while (result < x)
        {
            result = result * 10 + x % 10
            x = Math.trunc(x / 10)
        }
        return Object.is(result, x) || Object.is(Math.trunc(result / 10), x)
    }  
};
