class Solution {
    public int reverse(int x) {
        var result = 0;
        while (x != 0)
            if (Math.abs(result) > Integer.MAX_VALUE / 10) return 0;
            else
            {
                result = result * 10 + x % 10;
                x /= 10;
            }
        return result;
    }
}
