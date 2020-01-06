class Solution {
public:
    void reverseString(vector<char>& s) {
        if (std::empty(s)) return;
        auto left{std::begin(s)}, right{--std::end(s)};
        while (std::distance(left, right) > 0)
        {
            std::iter_swap(left, right);
            ++left;
            --right;
        }
    }
};
