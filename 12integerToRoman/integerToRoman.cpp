class Solution {
public:
    string intToRoman(int num) {
        std::vector const roman{std::pair{"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400}, {"C", 100}, {"XC", 90}, {"L", 50}, {"XL", 40}, {"X", 10}, {"IX", 9}, {"V", 5}, {"IV", 4}, {"I", 1}};
        std::stringstream result;
        for (auto const _: roman)
        {
            for (auto repeat{0}; repeat != num / _.second; ++repeat) result << _.first;
            num %= _.second;
        }
        return result.str();
    }
};
