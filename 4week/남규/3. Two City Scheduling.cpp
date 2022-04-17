// https://leetcode.com/problems/two-city-scheduling/

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        priority_queue<vector<int>> pq;
        for(auto cost : costs){
            pq.push({cost[0] - cost[1], cost[0], cost[1]});
        }
        
        int n = costs.size() / 2;
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            ans += pq.top()[2];
            pq.pop();
        }
        
        for(int i = 0; i < n; i++){
            ans += pq.top()[1];
            pq.pop();
        }
        return ans;
    }
};
