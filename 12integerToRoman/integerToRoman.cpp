class Solution {
public:
    string intToRoman(int num) {
        std::vector const roman{std::pair{"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400}, {"C", 100}, {"XC", 90}, {"L", 50}, {"XL", 40}, {"X", 10}, {"IX", 9}, {"V", 5}, {"IV", 4}, {"I", 1}};
        std::stringstream result;
        std::for_each(std::cbegin(roman), std::cend(roman), [&](auto const _){
            auto const [symbol, value]{_};
            for (std::size_t _{}; _ != num / value; ++_) result << symbol;
            num %= value;});
        return result.str();
    }
};
