class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> stk;
        
        for(auto token : tokens){
            if((token == "+") || (token == "-") || (token == "*") || (token == "/")){
                int operand2 = stoi(stk.top());
                stk.pop();
                int operand1 = stoi(stk.top());
                stk.pop();
                
                if(token == "+"){
                    stk.push(to_string(operand1 + operand2));
                } else if(token == "-"){
                    stk.push(to_string(operand1 - operand2));
                } else if(token == "*"){
                    stk.push(to_string(operand1 * operand2));
                } else if(token == "/"){
                    stk.push(to_string(operand1 / operand2));
                }
            } else {
                stk.push(token);
            }
        }
        return stoi(stk.top());
    }
};
