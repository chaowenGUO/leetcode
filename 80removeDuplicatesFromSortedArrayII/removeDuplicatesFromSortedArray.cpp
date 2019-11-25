class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::size_t index{0};
        std::for_each(std::cbegin(nums), std::cend(nums), [&](auto const num){
            if (index < 2 || num > nums.at(index - 2))
            {
                nums.at(index) = num;
                ++index;
            }});
        return index;
    }
};
