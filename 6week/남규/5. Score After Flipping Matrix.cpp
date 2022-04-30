class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int N = grid.size();
        int M = grid[0].size();
        
        for(int i = 0; i < N; i++){
            if(grid[i][0] == 0){
                for(int j = 0; j < M; j++){
                    grid[i][j] ^= 1;
                }
            }
        }
        
        for(int i = 1; i < M; i++){
            int cnt = 0;
            for(int j = 0; j < N; j++){
                if(grid[j][i] == 1){
                    cnt++;
                }
            }
            
            if(cnt > N / 2){
                continue;
            }
            
            for(int j = 0; j < N; j++){
                grid[j][i] ^= 1;
            }
        }
        
        int ans = 0;
        
        for(int i = 0; i < N; i++){
            int a = 0;
            for(int j = 0; j < M; j++){
                a *= 2;
                a += grid[i][j];
            }
            ans += a;
        }
        return ans;
    }
};
