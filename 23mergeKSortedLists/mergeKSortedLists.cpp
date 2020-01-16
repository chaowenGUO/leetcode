/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto const compare{[](auto const a, auto const b){return a->val > b->val;}};
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(compare)> queue{compare};
        for (auto&_: lists)
            while (_)
            {
                queue.emplace(_);
                _ = _->next;
            }
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        while (!std::empty(queue))
        {
            current->next = queue.top();
            queue.pop();
            current = current->next;
        }
        current->next = nullptr;
        return result->next;
    }
};
