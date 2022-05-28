class NumMatrix {
public:
    vector<long long> seg;
    int N, M;
    
    NumMatrix(vector<vector<int>>& matrix) {
        this->N = matrix.size();
        this->M = matrix[0].size();
        seg.resize(N * M * 2);
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                seg[N * M + M * i + j] = matrix[i][j];
            }
        }
        
        for(int i = N * M - 1; i > 0; i--){
            seg[i] = seg[2 * i] + seg[2 * i + 1];
        }
    }
    
    void update(int row, int col, int val) {
        int index = N * M + M * row + col;
        seg[index] = val;
        
        int left = index;
        int right = index;
        
        while(left != 1){
            if(left % 2 == 1){
                left--;
            } else {
                right++;
            }
            
            seg[left / 2] = seg[left] + seg[right];
            left /= 2;
            right /= 2;
        }
        return;
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int ret = 0;
        
        for(int row = row1; row <= row2; row++){
            int left = N * M + M * row + col1;
            int right = N * M + M * row + col2;
            
            while(left <= right){
                if(left == right){
                    ret += seg[left];
                    break;
                }

                if(left % 2 == 1){
                    ret += seg[left];
                    left++;
                }

                if(right % 2 == 0){
                    ret += seg[right];
                    right--;
                }

                left /= 2;
                right /= 2;
            }
        }
        return ret;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * obj->update(row,col,val);
 * int param_2 = obj->sumRegion(row1,col1,row2,col2);
 */
