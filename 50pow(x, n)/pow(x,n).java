class Solution {
    public double myPow(double x, int n) {
        double result = 1;
        final double sign = Math.signum(n);
        while (n != 0)
        {
            if ((n & 1) != 0) result *= x;
            x *= x;
            n /= 2;
        }
        return sign == 1 ? result : 1 / result;
    }
}
