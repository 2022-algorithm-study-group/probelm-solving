// 처음 보자마자 떠올린 솔루션(TLE)
class Solution {
public:
    int cache[41][41][1601];
    int ans = INT_MAX;
    
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    unordered_map<int, int> m;
    
    void traverse(vector<vector<int>>& grid, int y, int x, int k, int len, int prev){
        int N = grid.size();
        int M = grid[0].size();;
        
        if((y == N - 1) && (x == M - 1)){
            ans = min(ans, len);
            return;
        }
        
        int &ret = cache[y][x][k];
        if(ret != -1){
            if(ret <= len){
                return;
            }
        }
        
        ret = len;
        
        for(int i = 0; i < dirs.size(); i++){
            if(prev == m[i]) continue;
            
            int nextY = y + dirs[i][0];
            int nextX = x + dirs[i][1];
            
            if(nextY < 0 || nextY >= N || nextX < 0 || nextX >= M){
                continue;
            }
            
            if(grid[nextY][nextX] == 1 && k > 0){
                traverse(grid, nextY, nextX, k - 1, len + 1, i);
            } else if(grid[nextY][nextX] == 0){
                traverse(grid, nextY, nextX, k, len + 1, i);
            }
        }
    }
    
    int shortestPath(vector<vector<int>>& grid, int k) {
        m[0] = 1;
        m[1] = 0;
        m[2] = 3;
        m[3] = 2;
        memset(cache, -1, sizeof(cache));
        traverse(grid, 0, 0, k, 0, -1);
        return ans == INT_MAX ? -1 : ans;
    }
};


// Accepted

/*

Approach
1. cache N*M, A value of (i, j) is current remaining K
2. BFS (All elements inside of queue have a same step)
3. if (i, i) is (N - 1, M - 1), return step immedietely

Time Complexity: O(NMK)
Space Complexity: O(NMK) for Queue

*/

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int N = grid.size();
        int M = grid[0].size();
        
        int cache[41][41];
        memset(cache, -1, sizeof(cache));
        queue<vector<int>> que;
        que.push({0, 0, k});
        cache[0][0] = k;
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int step = 0;
        
        while(!que.empty()){
            int len = que.size();
            for(int i = 0; i < len; i++){
                int y = que.front()[0];
                int x = que.front()[1];
                int currK = que.front()[2];
                
                if((y == N - 1) && (x == M - 1)){
                    return step;
                }
                
                que.pop();
                
                for(auto direction : directions){
                    int nextY = y + direction[0];
                    int nextX = x + direction[1];
                    
                    if(nextY >= N || nextY < 0 || nextX >= M || nextX < 0){
                        continue;
                    }
                    
                    if(grid[nextY][nextX] == 1){
                        if(cache[nextY][nextX] < currK - 1){
                            cache[nextY][nextX] = currK - 1;
                            que.push({nextY, nextX, currK - 1});
                        }
                    } else if(grid[nextY][nextX] == 0){
                        if(cache[nextY][nextX] < currK){
                            cache[nextY][nextX] = currK;
                            que.push({nextY, nextX, currK});
                        }
                    }
                }
            }
            step++;
        }
        return -1;
    }
};
