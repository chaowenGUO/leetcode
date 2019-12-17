class Solution {
public:
    int uniquePaths(int m, int n) {
        std::size_t result{1};
        for (std::size_t _{1}; _ != m; ++_) result = result * (n - 1 + _) / _;
        return result;
    }
};
