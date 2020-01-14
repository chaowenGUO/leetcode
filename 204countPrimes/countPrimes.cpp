class Solution {
public:
    int countPrimes(int n) {
        if (n < 2) return 0;
        else
        {
            std::vector<int> result(n, 1);
            result.front() = result.at(1) = 0;
            for (std::size_t i{2}; i != static_cast<int>(std::sqrt(n)) + 1; ++i)
                for (std::size_t j{std::pow(i, 2)}; j < n; j += i) result.at(j) = 0;
            return std::accumulate(std::cbegin(result), std::cend(result), 0);
        }
    }
};
