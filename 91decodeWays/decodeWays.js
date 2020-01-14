/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    s = [...s]
    if (Object.is(s[0], '0')) return 0
    else
    {
        let [a, b, c] = [1, 1, 0]
        for (let _ = 1; !Object.is(_, s.length); ++_)
        {
            if (!Object.is(s[_], '0')) c = b
            const slice = s.slice(_ - 1, _ + 1).join('')
            if ('10' <= slice && slice <= '26') c += a;
            [a, b, c] = [b, c, 0]
        }
        return b
    }
};
