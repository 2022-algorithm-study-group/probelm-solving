class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        deque<int> que;
        int N = nums.size();
        
        int left = 0, right = 0;
        while(right < k) {
            if(!que.empty()) 
                while(!que.empty() && que.back() < nums[right]) 
                    que.pop_back();
            
            que.push_back(nums[right]);
            right++;
        }
        
        ans.push_back(que.front());
        
        while(right < N) {
            if(que.front() == nums[left]) 
                que.pop_front();
            left++;
            
            while(!que.empty() && que.back() < nums[right]) 
                que.pop_back();
            que.push_back(nums[right]);
            right++;
            
            ans.push_back(que.front());
        }
        return ans;
    }
};
