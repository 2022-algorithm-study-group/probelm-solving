class Solution {
public:
    int visited[201][201];
    int trapRainWater(vector<vector<int>>& heightMap) {
        int N = heightMap.size();
        int M = heightMap[0].size();
        priority_queue<vector<int>> pq;
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(i == 0 || j == 0 || i == N - 1 || j == M - 1){
                    pq.push({-heightMap[i][j], i, j});
                    visited[i][j] = 1;
                }
            }
        }
        
        int ys[4] = {0, 1, 0, -1};
        int xs[4] = {1, 0, -1, 0};
        int ans = 0;
        
        while(!pq.empty()){
            int currVal = -pq.top()[0];
            int y = pq.top()[1];
            int x = pq.top()[2];
            pq.pop();
            
            for(int i = 0; i < 4; i++){
                int nextY = y + ys[i];
                int nextX = x + xs[i];
                if(nextY < 0 || nextY >= N || nextX < 0 || nextX >= M){
                    continue;
                }
                
                if(visited[nextY][nextX]){
                    continue;
                }
                visited[nextY][nextX] = 1;
                
                int nextVal = heightMap[nextY][nextX];
                ans += max(0, currVal - nextVal);
                pq.push({-max(currVal, nextVal), nextY, nextX});
            }
        }
        return ans;
    }
};
