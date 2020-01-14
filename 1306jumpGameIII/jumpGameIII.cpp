class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        std::deque queue{start};
        std::unordered_set seen{start};
        while (!std::empty(queue))
        {
            auto const index{queue.front()};
            queue.pop_front();
            if (!arr.at(index)) return true;
            else
            {
                std::unordered_set child{index + arr.at(index), index - arr.at(index)};
                for (auto _{std::cbegin(child)}; _ != std::cend(child);) *_ < 0 || *_ >= std::size(arr) ? _ = child.erase(_) : ++_;
                for (auto _{std::cbegin(child)}; _ != std::cend(child);) seen.find(*_) != std::cend(seen) ? _ = child.erase(_) : ++_;
                queue.insert(std::cend(queue), std::cbegin(child), std::cend(child));
                seen.merge(child);
            }
        }
        return false;
    }
};
