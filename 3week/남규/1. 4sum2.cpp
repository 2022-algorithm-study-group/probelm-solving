class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> cache;
        
        // -> k sum?
      
        for(int i = 0; i < nums1.size(); i++){
            for(int j = 0; j < nums2.size(); j++){
                int ab = -nums1[i] - nums2[j];
                cache[ab]++;
            }
        }
        
        int ans = 0;
        
        for(int i = 0; i < nums3.size(); i++){
            for(int j = 0; j < nums4.size(); j++){
                int cd = nums3[i] + nums4[j];
                ans += cache[cd];
            }
        }
        return ans;
    }
};
