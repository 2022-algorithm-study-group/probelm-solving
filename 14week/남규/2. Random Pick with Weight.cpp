class Solution {
public:
    vector<int> partialSum;
    
    Solution(vector<int>& w) {
        for(auto v : w){
            if(partialSum.empty()){
                partialSum.push_back(v);
            } else {
                partialSum.push_back(partialSum.back() + v);
            }
        }
    }
    
    int pickIndex() {
        double pick = (double)rand() / RAND_MAX;
        double target = pick * partialSum.back();
        
        return upper_bound(partialSum.begin(), partialSum.end(), target) - begin(partialSum);
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
