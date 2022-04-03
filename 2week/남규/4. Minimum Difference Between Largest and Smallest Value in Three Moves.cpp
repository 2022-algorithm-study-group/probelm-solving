class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        
        // TC1
        // [1,2,3]
        // return 0
        
        // TC2
        // [1,2,3,4,5]
        // return 1
        
        // TC3
        // [0, 3, 9, 10, 13, 18]
        // return 4
        
        // Time Complexity: O(N log N)
        // Space Complexity: O(1)
        
        if (n < 5) return 0;
        sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        
        for(int i = 0; i < 4; i++){
            ans = min(ans, nums[n - 4 + i] - nums[i]);
        }
        return ans;
        
        // 0, 1, 5, 10, 14, 15
    }
};
