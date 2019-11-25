class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::size_t index{std::empty(nums) ? 0 : 1};
        std::for_each(std::cbegin(nums), std::cend(nums), [&](auto const num){
            if (num > nums.at(index - 1))
            {
                nums.at(index) = num;
                ++index;
            }});
        return index;
    }
};
