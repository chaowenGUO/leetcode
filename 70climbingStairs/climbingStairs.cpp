class Solution {
public:
    int climbStairs(int n) {
        std::array result{1, 1};
        for (std::size_t _{0}; _ != n; ++_) result = {result.back(), result.front() + result.back()};
        return result.front();
    }
};
