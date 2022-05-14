class Solution {
public:
    int cache[5001][301];
    
    int dfs(int amount, int pos, vector<int>& coins){
        if(amount == 0) return 1;
        if(amount < 0) return 0;
        if(pos >= coins.size()) return 0;
        int& ret = cache[amount][pos];
        if(ret != -1) return ret;
        ret = 0;
        
        return ret = dfs(amount - coins[pos], pos, coins) + dfs(amount, pos + 1, coins);
    }
    
    int change(int amount, vector<int>& coins) {
        memset(cache, -1, sizeof(cache));
        return dfs(amount, 0, coins);
    }
};
