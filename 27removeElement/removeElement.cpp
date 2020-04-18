class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        return std::distance(std::begin(nums), std::remove(std::begin(nums), std::end(nums), val));
    }
};
