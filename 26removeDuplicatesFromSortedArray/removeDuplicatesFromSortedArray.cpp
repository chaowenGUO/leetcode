class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        return std::distance(std::begin(nums), std::unique(std::begin(nums), std::end(nums)));
    }
};
