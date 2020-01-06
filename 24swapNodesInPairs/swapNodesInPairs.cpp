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
    ListNode* swapPairs(ListNode* head) {
        auto const result{std::make_unique<ListNode>(0)};
        auto current{result.get()};
        current->next = head;
        decltype(head) a;
        while ((a = current->next) && current->next->next)
        {
            current->next = current->next->next;
            a->next = a->next->next;
            current->next->next = a;
            current = a;
        }
    return result->next;
    }
};
