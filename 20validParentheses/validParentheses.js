/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const parentheses = Object.freeze({'{':'}', '[':']', '(':')'})
    stack = []
    for (const _ of s)
        if (_ in parentheses) stack.push(parentheses[_])
        else if (!stack.length || !Object.is(stack.pop(), _)) return false 
    return !stack.length
};
