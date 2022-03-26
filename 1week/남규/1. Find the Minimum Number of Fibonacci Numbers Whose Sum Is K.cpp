class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        vector<int> fibo = {1, 1};
        
        // Time Complexity: O(N), N is a length of fibonacci numbers
        // Space Complexity: O(N)
        
        // Approach: greedy
        
        for(int i = 2; true; i++){
            int target = fibo[i - 1] + fibo[i - 2];
            if(target > k){
                break;
            }
            fibo.push_back(target);
        }
        
        int ans = 0;
        
        for(int i = fibo.size() - 1; i >= 0; i--){
            while(fibo[i] <= k){
                k -= fibo[i];
                ans++;
            }
            if(k == 0) break;
        }
        return ans;
    }
};
