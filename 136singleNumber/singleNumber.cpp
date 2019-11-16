class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return std::accumulate(std::cbegin(nums), std::cend(nums), 0, std::bit_xor{});
    }
};
