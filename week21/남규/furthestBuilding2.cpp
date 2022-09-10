class Solution {
public:
    bool canReach(vector<int>& heights, int end, int bricks, int ladders) {
        vector<int> diffs;
        for(int i = 0; i < end; i++) {
            int curr = heights[i];
            int next = heights[i + 1];
            
            if(next - curr > 0) {
                diffs.push_back(next - curr);
            }
        }
        
        sort(diffs.begin(), diffs.end());
        
        for(int i = 0; i < diffs.size(); i++) {
            if(diffs[i] <= bricks) {
                bricks -= diffs[i];
            } else {
                ladders--;
            }
            
            if(ladders < 0) return false;
        }
        
        return true;
    }
    
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int left = 0, right = heights.size() - 1;
        
        while(left < right) {
            int mid = left + (right - left + 1) / 2;
            
            if(canReach(heights, mid, bricks, ladders)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
};
