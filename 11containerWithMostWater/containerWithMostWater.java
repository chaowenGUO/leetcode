class Solution {
    public int maxArea(int[] height) {
        var left = 0;
        var right = height.length - 1;
        var result = 0;
        while (left != right)
        {
            result = Math.max(result, (right - left) * IntStream.of(left, right).map($ -> height[$]).min().orElse(0));
            var $$ = IntStream.of(left, right).map($ -> height[$]).reduce((a,b) -> a - b).orElse(0) < 0 ? ++left : --right;
        }
        return result;
    }
}
