class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int result = 0;
        while (left != right)
        {
            result = Math.max(result, (right - left) * IntStream.of(left, right).map($ -> height[$]).min().orElse(0));
            int $$ = IntStream.of(left, right).map($ -> height[$]).reduce((a,b) -> a - b).orElse(0) < 0 ? ++left : --right;
        }
        return result;
    }
}
