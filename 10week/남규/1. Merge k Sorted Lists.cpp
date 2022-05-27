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
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<pair<int, ListNode*>> pq;
        
        for(auto list : lists){
            if(list == NULL) continue;
            pq.push({-list->val, list});
        }
        
        ListNode* prev = new ListNode(-1);
        ListNode* curr = NULL;
        
        while(!pq.empty()){
            int leastVal = -pq.top().first;
            ListNode* leastList  = pq.top().second;
            pq.pop();
            
            if(curr == NULL){
                curr = leastList;
                prev->next = curr;
            } else {
                curr->next = leastList;
                curr = curr->next;
            }
            
            if(leastList->next){
                pq.push({-leastList->next->val, leastList->next});
            }
        }
        return prev->next;
    }
};
