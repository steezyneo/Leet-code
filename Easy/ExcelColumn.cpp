#include<iostream>    

using namespace std;

int titleToNumber(string columnTitle) {
    int result = 0;
    for (char c : columnTitle) {
        int d = c - 'A' + 1;
        result = result * 26 + d;
    }
    return result;
}

int main(){
    string s = "AB";
    // int c = 'Z' - 'A' + 1;
    // cout<<c;
    cout<<titleToNumber(s);
}