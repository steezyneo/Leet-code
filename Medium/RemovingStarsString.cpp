#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

string removeStars(string s) {
    stack<char> st;
    for(int i=0; i<s.size(); i++){
        if(s[i] != '*'){
            st.push(s[i]);
        }else{
            st.pop();
        }
    }
    string newStr = "";
    while(!st.empty()){
        newStr += st.top();
        st.pop();
    }
    reverse(newStr.begin(), newStr.end());
    return newStr;
}

int main(){
    string s = "leet**cod*e";
    string newStr = removeStars(s);
    cout << newStr;
    return 0;
}