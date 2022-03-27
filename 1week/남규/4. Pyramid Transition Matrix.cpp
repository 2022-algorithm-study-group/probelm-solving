// https://leetcode.com/problems/pyramid-transition-matrix/

class Solution {
public:
    char matrix[7][7];
    unordered_map<string, vector<char>> strToChar;
    unordered_set<string> cache;
    int N;
    
    bool traverse(int row, int column, string& rowStr){
        if(row == N){
            return true;
        }
        
        bool ret = false;
        
        string s = "";
        s += matrix[row - 1][column];
        s += matrix[row - 1][column + 1];
        
        for(int i = 0; i < strToChar[s].size(); i++){
            char c = strToChar[s][i];
            matrix[row][column] = c;

            rowStr.push_back(c);
            if(column + 1 >= N - row){
                if(cache.find(rowStr) != cache.end()){
                    // 무시
                    ret |= false;
                } else {
                    string tmp = "";
                    ret |= traverse(row + 1, 0, tmp);
                    cache.insert(rowStr);
                }
            } else {
                ret |= traverse(row, column + 1, rowStr);
            }
            if(ret) return true;
            rowStr.pop_back();
        }
        return ret;
    }
    
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        int N = bottom.size();
        this->N = N;
        for(int i = 0; i < N; i++){
            matrix[0][i] = bottom[i];
        }
        
        for(int i = 0; i < allowed.size(); i++){
            string s = "";
            s += allowed[i][0];
            s += allowed[i][1];
            strToChar[s].push_back(allowed[i][2]);
        }
        string rowStr = "";
        return traverse(1, 0, rowStr);
    }
};
