class Solution {
public:
    // 생각안하고 풀면 dp로 잘못 풀 수 있음
    
    int maxScore(vector<int>& cardPoints, int k) {
        int race = 0;
        for(int i = 0; i < k; i++){
            race += cardPoints[i];
        }
        
        int left = k - 1;
        int right = cardPoints.size() - 1;
        int ans = race;
        
        while(left >= 0){
            race -= cardPoints[left--];
            race += cardPoints[right--];
            ans = max(ans, race);
        }
        return ans;
    }
};
