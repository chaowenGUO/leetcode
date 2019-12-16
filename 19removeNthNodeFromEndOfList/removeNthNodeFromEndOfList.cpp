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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto fast{head}, slow{head};
        for (std::size_t _{}; _ != n; ++_) fast = fast->next;
        if (!fast) return head->next;
        else
        {
            while (fast->next)
            {
                fast = fast->next;
                slow = slow->next;
            }
            slow->next = slow->next->next;
            return head;
        }
    }
};
