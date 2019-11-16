class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || x != 0 && x % 10 == 0) return false;
        else
        {
            auto result{0};
            while (result < x)
            {
                result = result * 10 + x % 10;
                x /= 10;
            }
            return result == x || result / 10 == x;
        }
    }
};
