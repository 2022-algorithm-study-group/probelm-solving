class Solution {
public:
    int maxArea(vector<int>& height) {
        int N = height.size();
        int left = 0;
        int right = N - 1;
        int ans = 0;
        
        while(left < right){
            int diff = right - left;
            if(height[left] < height[right]){
                ans = max(ans, diff * height[left]);
                left++;
            } else if(height[left] > height[right]){
                ans = max(ans, diff * height[right]);
                right--;
            } else {
                ans = max(ans, diff * height[left]);
                left++;
                right--;
            }
        }
        return ans;
    }
};
