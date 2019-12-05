/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
        const result = []
        for (const interval of intervals.sort((a,b) => a[0] - b[0]))
        {
            if (result.length && interval[0] <= result[result.length - 1][1]) result[result.length - 1][1] = Math.max(result[result.length - 1][1], interval[1])
            else result.push(interval)
        }
        return result
};
