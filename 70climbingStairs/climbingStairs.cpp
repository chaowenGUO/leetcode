class Solution {
public:
    int climbStairs(int n) {
        std::array result{1l, 1l};
        for (std::size_t _{}; _ != n; ++_) result = {result.back(), result.front() + result.back()};
        return result.front();
    }
};
