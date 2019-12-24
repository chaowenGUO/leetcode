class Solution {
public:
    bool isNumber(string s) {
        std::regex const regex{R"(^\s*[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?\s*$)"};
        return std::regex_match(s, regex);
    }
};
