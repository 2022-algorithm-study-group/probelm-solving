//https://leetcode.com/problems/map-of-highest-peak/

class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int N = isWater.size();
        int M = isWater[0].size();
        vector<vector<int>> ans(N, vector<int>(M, -1));
        
        queue<vector<int>> que;
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(isWater[i][j]){
                    que.push({i, j});
                    ans[i][j] = 0;
                }
            }
        }
        
        int ys[4] = {1, 0, -1, 0};
        int xs[4] = {0, 1, 0, -1};
        
        if(que.empty()){
            ans.resize(N, vector<int>(M, 0));
            return ans;
        }
        
        while(!que.empty()){
            int y = que.front()[0];
            int x = que.front()[1];
            que.pop();
            
            for(int i = 0; i < 4; i++){
                int nextY = y + ys[i];
                int nextX = x + xs[i];
                
                if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= M){
                    continue;
                }
                
                if(ans[nextY][nextX] != -1){
                    continue;
                }
                ans[nextY][nextX] = ans[y][x] + 1;
                que.push({nextY, nextX});
            }
        }
        return ans;
    }
};
