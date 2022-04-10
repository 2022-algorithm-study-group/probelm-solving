class Solution {
public:
    int dfs(vector<int>& coins, vector<vector<int>>& dp, int remain, int index){
        int N = coins.size();
        if(remain == 0) return 0;
        if(index >= N) return INT_MAX;
        
        int &ret = dp[remain][index];
        if(ret != -1) return ret;
        ret = INT_MAX;
        
        if(remain - coins[index] >= 0){
            int cand = dfs(coins, dp, remain - coins[index], index);
            cand = cand == INT_MAX ? cand : cand + 1;
            ret = min(ret, cand);
        }
        ret = min(ret, dfs(coins, dp, remain, index + 1));
        return ret;              
    }
    
    int coinChange(vector<int>& coins, int amount) {
        if(amount == 0) return 0;
        int N = coins.size();
        vector<vector<int>> dp(amount + 1, vector<int>(N, -1));
        int ans = dfs(coins, dp, amount, 0);
        return ans == INT_MAX ? -1 : ans;
    }
};
