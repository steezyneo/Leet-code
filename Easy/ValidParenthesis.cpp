#include <iostream>
#include <stack>

using namespace std;

bool isValid(string s) {
    stack<char> stk;

    for(char c : s){
        if(c == '(' || c=='[' || c=='{')
            stk.push(c);
        else if(c == ')' && !stk.empty() && stk.top() == '(')
            stk.pop();
        else if(c == ']' && !stk.empty() && stk.top() == '[')
            stk.pop();
        else if(c == '}' && !stk.empty() && stk.top() == '{')
            stk.pop();
        else
            return false;
    }
    return stk.empty();
}

int main(){
    string str = "([])";
    if(isValid(str))
        cout<< "true";
    else    
        cout<< "false";
}