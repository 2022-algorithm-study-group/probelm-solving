class Solution {
public:
    int cache[10][10];
    int rows[10];
    int cols[10];
    bool isFinished = false;
    
    bool sudokuValid(int y, int x, int num){
        int y3 = y / 3;
        int x3 = x / 3;
        
        if(cache[y3][x3] & (1 << num)){
            return false;
        }
        
        if(rows[y] & (1 << num)){
            return false;
        }
        
        if(cols[x] & (1 << num)){
            return false;
        }
        
        return true;
    }
    
    void backtrack(vector<vector<char>>& board, int y, int x, int N, int M){
        if(x == M){
            y += 1;
            x = 0;
        }
        
        if(y == N){
            isFinished = true;
            return;
        }
        
        if(board[y][x] == '.'){
            for(int num = 1; num < 10; num++){
                if(sudokuValid(y, x, num)){
                    board[y][x] = '0' + num;

                    cache[y / 3][x / 3] |= (1 << num);
                    rows[y] |= (1 << num);
                    cols[x] |= (1 << num);
                    backtrack(board, y, x + 1, N, M);
                    if(isFinished) return;

                    cache[y / 3][x / 3] ^= (1 << num);
                    rows[y] ^= (1 << num);
                    cols[x] ^= (1 << num);

                    board[y][x] = '.';
                }
            }
        } else {
            backtrack(board, y, x + 1, N, M);
        }
    }
    
    void solveSudoku(vector<vector<char>>& board) {
        int N = board.size();
        int M = board[0].size();
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                int y = i / 3;
                int x = j / 3;
                if(board[i][j] == '.') continue;
                int val = board[i][j] - '0';
                cache[y][x] |= (1 << val);
                rows[i] |= (1 << val);
                cols[j] |= (1 << val);
            }
        }
        
        backtrack(board, 0, 0, N, M);
    }
};
