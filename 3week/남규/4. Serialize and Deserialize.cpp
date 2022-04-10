/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    string bfs(TreeNode* node){
        string ret = "[";
        queue<TreeNode*> que;
        
        int normals = 1;
        que.push(node);
        
        while(!que.empty()){
            if(normals == 0){
                break;
            }
            
            TreeNode* cur = que.front();
            que.pop();
            
            if(cur) {
                normals--;
                ret += to_string(cur->val) + ",";
                
                que.push(cur->left);
                if(cur->left){
                    normals++;
                }
                que.push(cur->right);
                if(cur->right){
                    normals++;
                }
            } else {
                ret += "null,";
            }
        }
        ret[ret.size() - 1] = ']';
        return ret;
    }
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(!root){
            return "[]";
        }
        return bfs(root);
    }

    vector<int> tokens;
    
    TreeNode* deserializeLoop(){
        TreeNode* node = new TreeNode(tokens[0]);
        queue<TreeNode*> que;
        que.push(node);
        int pos = 1;
        
        while(!que.empty()){
            if(pos >= tokens.size()) break;
            TreeNode* cur = que.front();
            que.pop();
            
            if(cur == NULL) continue;
            
            if(pos < tokens.size() && tokens[pos] != -1001){
                cur->left = new TreeNode(tokens[pos]);    
            }
            if(pos + 1 < tokens.size() && tokens[pos + 1] != -1001)
                cur->right = new TreeNode(tokens[pos + 1]);
            pos += 2;
            
            que.push(cur->left);
            que.push(cur->right);
        }
        return node;
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        string token = "";
        for(int i = 1; i < data.size(); i++){
            if(data[i] == ',' || data[i] == ']'){
                if(token == "") continue;
                
                if(token == "null"){
                    tokens.push_back(-1001);
                } else {
                    int t = stoi(token);
                    tokens.push_back(t);    
                }
                token = "";
                continue;
            }
            token += data[i];
        } 
        
        if(tokens.empty()) return NULL;
        return deserializeLoop();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
