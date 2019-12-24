class Solution {
public:
    int singleNumber(vector<int>& nums) {
        auto [a, b]{std::array<int, 2>{}};
        std::for_each(std::cbegin(nums), std::cend(nums), [&](auto const num){
            b = (b ^ num) & ~a;
            a = (a ^ num) & ~b;});
        return b;
    }
};
