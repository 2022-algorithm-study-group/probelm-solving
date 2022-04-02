class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> points;
        for(auto timePoint : timePoints){
            int h1 = timePoint[0] - '0';
            int h2 = timePoint[1] - '0';
            int m1 = timePoint[3] - '0';
            int m2 = timePoint[4] - '0';
            
            int v = m2 + m1 * 10 + h2 * 60 + h1 * 60 * 10;
            points.push_back(v);
        }
        
        sort(points.begin(), points.end());
        int ans = INT_MAX;
        
        for(int i = 0; i < points.size() - 1; i++){
            int diff = points[i + 1] - points[i];
            ans = min(ans, diff);
        }
        return min(ans, points[0] + 1440 - points.back());
    }
};
