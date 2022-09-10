class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int> minQue;
        
        for(int i = 0; i < heights.size() - 1; i++) {
            int curr = heights[i];
            int next = heights[i + 1];
            
            if(curr >= next) continue;
            
            if(bricks == 0) return i;
            
            if(curr < next) {
                minQue.push(-(next - curr));
            }
            
            if(minQue.size() > ladders) {
                if(bricks + minQue.top() < 0) return i;
                bricks += minQue.top();
                minQue.pop();
            }
        }
        return heights.size() - 1;
    }
};
