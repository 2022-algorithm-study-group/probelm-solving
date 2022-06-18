class Solution {
public:
    unordered_map<int, unordered_map<int, int>> matrix;
    
    int minAreaRect(vector<vector<int>>& points) {
        for(auto point : points) {
            int y = point[0];
            int x = point[1];
            matrix[y][x] = 1;
        }
        
        int N = points.size();
        int ans = INT_MAX;
        
        for(int i = 0; i < N; i++){
            int y = points[i][0];
            int x = points[i][1];
            for(int j = i + 1; j < N; j++){
                int nextY = points[j][0];
                int nextX = points[j][1];
                
                if(y == nextY || x == nextX) continue;
                if(matrix[y][nextX] && matrix[nextY][x]){
                    ans = min(ans, abs(nextY - y) * abs(nextX - x));
                }
            }
        }
        return ans == INT_MAX ? 0 : ans;
    }
};
