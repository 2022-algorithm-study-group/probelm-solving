class Solution {
public:
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
