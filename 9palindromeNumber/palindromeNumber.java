class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || x != 0 && x % 10 == 0) return false;
        else
        {
            var result = 0;
            while (result < x)
            {
                result = result * 10 + x % 10;
                x /= 10;
            }
            return result == x || result / 10 == x;
        }
    }
}
