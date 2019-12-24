class Solution {
public:
    bool isPalindrome(string s) {
        s = std::regex_replace(s, std::regex{R"(\W)"}, "");
        std::transform(std::cbegin(s), std::cend(s), std::begin(s), [](auto const _){return std::tolower(_);});
        auto reverse{s};
        std::reverse(std::begin(s), std::end(s));
        return s == reverse;
    }
};
