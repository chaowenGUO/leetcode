class Solution {
    public int mySqrt(int x) {
        int left = 0, right = x / 2 + 1;
        while (left != right)
        {
            final int middle = left + (right - left) / 2;
            if (Math.pow(middle, 2) < x) left = middle + 1;
            else right = middle;
        }
        return Math.pow(left, 2) == x ? left : left - 1;
    }
}
