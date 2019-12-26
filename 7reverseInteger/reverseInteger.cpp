class Solution {
public:
    int reverse(int x) {
        auto result{0};
        while (x)
            if (std::abs(result) > std::numeric_limits<int>::max() / 10) return false;
            else
            {
                result = result * 10 + x % 10;
                x /= 10;
            }
        return result;
    }
};
