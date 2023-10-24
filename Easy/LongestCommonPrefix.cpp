#include<iostream>
#include<vector>

using namespace std;

string longestCommonPrefix(vector<string>& arr) {
    string pr;

    for (int i = 0; i < arr[0].length(); i++) { 
        char current_char = arr[0][i];
        for (int j = 1; j < arr.size(); j++) { 
            if (arr[j][i] != current_char) {
                return pr; 
            }
        }
        pr += current_char;
    }

    return pr;
}

int main() {
    vector<string> strs = {"flower", "flow", "flight"};
    cout << longestCommonPrefix(strs);
}
