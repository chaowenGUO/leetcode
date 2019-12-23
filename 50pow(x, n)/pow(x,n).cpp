class Solution {
public:
    double myPow(double x, int n) {
        auto result{1.};
        auto const sign{std::signbit(n)};
        while (n)
        {
            if (n & 1) result *= x;
            x *= x;
            n /= 2;
        }
        return sign ? 1 / result : result;
    }
};
