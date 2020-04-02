/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    s = [...s]
    let [result, left, right] = Array(3).fill(0)
    const characters = new Set
    while (right < s.length)
        if (!characters.has(s[right]))
        {
            characters.add(s[right++])
            result = Math.max(result, characters.size)
        }
        else characters.delete(s[left++])
    return result
};
