class Solution {
public:
    int reverse(int x) {
        auto result{0};
        while (x)
            if (std::abs(result) > std::numeric_limits<decltype(x)>::max() / 10) return 0;
            else
            {
                result = result * 10 + x % 10;
                x /= 10;
            }
        return result;
    }
};
