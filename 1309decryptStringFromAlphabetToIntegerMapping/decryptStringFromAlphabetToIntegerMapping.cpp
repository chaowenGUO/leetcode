class Solution {
public:
    string freqAlphabets(string s) {
        std::regex const regex{R"(\d{2}#|\d)"};
        std::sregex_iterator const begin{std::cbegin(s), std::cend(s), regex}, end;
        std::stringstream result;
        std::for_each(begin, end, [&result](auto const group){
            result << static_cast<char>(std::stoi(std::regex_replace(group.str(), std::regex{"#"}, "")) + 'a' - 1);});
        return result.str();
    }
};
