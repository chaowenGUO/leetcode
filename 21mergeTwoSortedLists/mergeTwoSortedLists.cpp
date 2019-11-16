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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        std::forward_list<decltype(std::declval<ListNode>().val)> linkedList;
        auto position{linkedList.cbefore_begin()};
        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                position = linkedList.emplace_after(position, l1->val);
                l1 = l1 ->next;
            }
            else
            {
                position = linkedList.emplace_after(position, l2 -> val);
                l2 = l2 ->next;
            }
        }
        auto l{l1 ? l1 : l2};
        while (l)
        {
            position = linkedList.emplace_after(position, l->val);
            l = l->next;
        }
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        std::for_each(std::cbegin(linkedList), std::cend(linkedList), [&current](auto const _){
            current->next = new ListNode{_};
            current = current->next;});
        return result->next;
    }
};
