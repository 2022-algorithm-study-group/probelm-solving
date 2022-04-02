class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int N = points[0].size();
        
        // Space Complexity: O(N)
        vector<long long> prev(N, 0), curr(N, 0);
        
        // Time Complexity: O(NM)
        for(auto point : points){
            long long race = 0;
            for(int i = 0; i < point.size(); i++){
                race = max(race - 1, prev[i]);
                curr[i] = race;
            }
            
            race = 0;
            for(int i = point.size() - 1; i >=0; i--){
                race = max(race - 1, prev[i]);
                curr[i] = max(curr[i], race) + point[i];
            }
            
            swap(prev, curr);
        }
        return *max_element(prev.begin(), prev.end());
    }
};
