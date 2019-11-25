class Solution {
public:
    int mySqrt(int x) {
        auto [left, right]{std::pair{0, x / 2 + 1}};
        while (left != right)
        {
            const auto middle{left + (right - left) / 2};
            if (std::pow(middle, 2) < x) left = middle + 1;
            else right = middle;
        }
        return std::pow(left, 2) == x ? left : left - 1;
    }
};
