/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

/*
TC1
Input: [1]
Output: 1
*/

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head || !head->next) return NULL;
        ListNode* prev = new ListNode(-1, head);
        ListNode* ans = prev;
        ListNode* slow = head;
        ListNode* fast = head->next;
        int slowLen = 0;
        int fastLen = 1;
        
        while(fast && fast->next){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
            slowLen += 1;
            fastLen += 2;
        }
        
        if(fast && !fast->next){
            fastLen++;
        }
        
        int target = fastLen - n;
        
        if(slowLen <= target){
            while(slow && slowLen < target){
                prev = slow;
                slow = slow->next;
                slowLen++;
            }
            prev->next = slow->next;
        } else if(slowLen > target){
            ListNode* curr = head;
            prev = ans;
            int race = 0;
            while(curr && race < target){
                prev = curr;
                curr = curr->next;
                race++;
            }
            prev->next = curr->next;
        }
        return ans->next;
    }
};
