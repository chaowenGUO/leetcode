class Solution {
public:
    string reverseStr(string s, int k) {
        for (std::size_t _{}; _ < std::size(s); _ += 2 * k) std::reverse(std::next(std::begin(s), _), std::min(std::next(std::begin(s), _ + k), std::end(s)));
        return s;
    }
};
