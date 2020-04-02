class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        else
        {
            std::vector<std::string> result(numRows);
            auto row{0}, direction{1};
            for (auto const _: s)
            {
                result.at(row) += _;
                if (row == 0) direction = 1;
                else if (row == numRows - 1) direction = -1;
                row += direction;
            }
            std::stringstream out;
            std::copy(std::cbegin(result), std::cend(result), std::ostream_iterator<std::string>{out});
            return out.str();
        }
    }
};
