class Solution {
    public int[] sumZero(int n) {
        return IntStream.range(1 - n, n).filter($ -> ($ - 1 + n & 1) == 0).toArray();
    }
}
