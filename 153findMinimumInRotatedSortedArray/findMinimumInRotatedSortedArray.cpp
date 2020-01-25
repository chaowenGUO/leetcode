class Solution {
public:
    int findMin(vector<int>& nums) {
        return *std::lower_bound(std::cbegin(nums), std::cend(nums), nums.back(), [](auto const middle, auto const value){
            return value < middle;
        });
    }
};
