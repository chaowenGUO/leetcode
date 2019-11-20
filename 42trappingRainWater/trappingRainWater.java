class Solution {
    public int trap(int[] height) {
        int result = 0, level = 0;
        int left = 0, right = height.length - 1;
        while (left < right)
        {
            final int low = java.util.stream.IntStream.of(left, right).map($ -> height[$]).min().orElse(0);
            int $_ = java.util.stream.IntStream.of(left, right).map($ -> height[$]).reduce((a ,b) -> a - b).orElse(0) < 0 ? ++left : --right;
            level = Math.max(level, low);
            result += level - low;
        }
        return result;
    }
}
