class RLEIterator {
public:
    deque<int> que;
    
    RLEIterator(vector<int>& encoding) {
        for(int i = 0; i < encoding.size(); i++) {
            que.push_back(encoding[i]);
        }
    }
    
    int next(int n) {
        int ret = -1;
        while(n && !que.empty()) {
            int top = que.front();
            que.pop_front();
            if(top >= n) {
                ret = que.front();
                que.push_front(top - n);
                break;
            }
            
            n -= top;
            que.pop_front();
            if(!que.empty())
                top = que.front();
        }
        return ret;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */
