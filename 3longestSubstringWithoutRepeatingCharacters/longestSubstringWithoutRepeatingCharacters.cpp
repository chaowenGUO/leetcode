class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::size_t result{};
        auto left{std::cbegin(s)}, right{std::cbegin(s)};
        std::unordered_set<decltype(s)::value_type> characters;
        while (right != std::cend(s))
            if (characters.find(*right) == std::cend(characters))
            {
                characters.emplace(*right++);
                result = std::max(result, std::size(characters));
            }
            else characters.extract(*left++);
        return result;
    }
};
