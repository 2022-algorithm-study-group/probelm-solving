class Solution {
public:
    int reverse(int x) {
        if(x == -pow(2, 31) || x == 0){
            return 0;
        }
        int ans = 0;
        
        if(x < 0){
            x = -x;
            while(x){
                if(ans > (pow(2, 31)) / 10) return 0;
                ans *= 10;
                ans += x % 10;
                x /= 10;
            }
            ans = -ans;
        } else if(x > 0){
            while(x){
                if(ans > (pow(2, 31) - 1) / 10) return 0;
                ans *= 10;
                ans += x % 10;
                x /= 10;
            }
        }
        return ans;
    }
};
