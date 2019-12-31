class Solution {
public:
    vector<int> sumZero(int n) {
        std::invoke_result_t<decltype(&Solution::sumZero), Solution, decltype(n)> result;
        for (std::ptrdiff_t _{1 - n}; _ < n; _ += 2) result.emplace_back(_);
        return result;
    }
};
