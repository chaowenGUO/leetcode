/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
    auto list(ListNode* list)
    {
        std::forward_list<decltype(std::declval<ListNode>().val)> result;
        auto position{result.cbefore_begin()};
        while (list)
        {
            position = result.emplace_after(position, list->val);
            list = list->next;
        }
        return result;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::forward_list<decltype(std::declval<ListNode>().val)> list;
        for (auto const&_: lists) list.merge(this->list(_));
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        for (auto const _: list)
        {
            current->next = new ListNode{_};
            current = current->next;
        }
        return result->next;
    }
};
