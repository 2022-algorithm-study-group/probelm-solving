class Solution {
public:
    bool removeOnes(vector<vector<int>>& grid) {
        int N = grid.size();
        int M = grid[0].size();
        
        for(int col = 0; col < M; col++){
            if(grid[0][col]){
                for(int row = 1; row < N; row++){
                    grid[row][col] = grid[row][col] ^ 1;
                }
            }
        }
        
        for(int row = 1; row < N; row++){
            for(int col = 1; col < M; col++){
                if(grid[row][col - 1] != grid[row][col]){
                    return false;
                }
            }
        }
        return true;
    }
};
