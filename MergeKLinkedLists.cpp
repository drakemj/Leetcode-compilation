/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 * 
 *      A reminder to use more priority queues. This is faster than 99.52% of submissions and is around 85% memorywise.
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, ListNodeCompare> p;
        for (auto& e: lists) if (e) p.push(e);
        ListNode* out = new ListNode();
        ListNode* prev = out;
        while (!p.empty()){
            ListNode* c = p.top();
            prev->next = c;
            prev = c;
            p.pop();
            if (c->next) p.push(c->next);
        }
        return out->next;
    }

    struct ListNodeCompare{
        bool operator() (ListNode* const& n1, ListNode* const& n2){
            return n1->val > n2->val;
        }
    };
};