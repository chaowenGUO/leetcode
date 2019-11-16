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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        std::forward_list<decltype(std::declval<ListNode>().val)> linkedList;
        auto position{linkedList.cbefore_begin()};
        auto carry{0};
        while (l1 || l2 || carry)
        {
            if (l1)
            {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2)
            {
                carry += l2->val;
                l2 = l2->next;
            }
            position = linkedList.emplace_after(position, carry % 10);
            carry /= 10;
        }
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        std::for_each(std::cbegin(linkedList), std::cend(linkedList), [&current](auto const _){
            current->next = new ListNode(_);
            current = current->next;});
        return result->next;
    }
};
