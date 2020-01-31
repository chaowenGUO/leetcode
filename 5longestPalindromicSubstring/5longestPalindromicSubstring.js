/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    const replace = [...'$#', ...s.replace(/\w/g, group => group + '#')]
    let center = 0, right = 0
    const radius = [...Array(replace.length).fill(0)]
    for (let _ = 1; !Object.is(_, replace.length); ++_)
    {
        radius[_] = right > _ ? Math.min(radius[2 * center - _], right - _) : 1
        while (replace[_ + radius[_]] == replace[_ - radius[_]]) ++radius[_]
        if (_ + radius[_] > right)
        {
            center = _
            right = _ + radius[_]
        }
    }
    center = radius.indexOf(Math.max(...radius))
    return s.slice((center - radius[center]) / 2, (center + radius[center]) / 2 - 1)
}
