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
        std::priority_queue<int, std::vector<int>, std::greater<int>> queue;
        for (auto list: lists)
        {
            while (list)
            {
                queue.emplace(list->val);
                list = list->next;
            }
        }
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        while (!queue.empty())
        {
            current->next = new ListNode(queue.top());
            queue.pop();
            current = current->next;
        }
        return result->next;
    }
};
