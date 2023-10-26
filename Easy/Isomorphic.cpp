#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

bool isIsomorphic(string s, string t) {

    if(s.length()!=t.length()) return 0;

    unordered_map<char, vector<int>> iso1;
    unordered_map<char, vector<int>> iso2;

    for(int i=0; i<s.length(); i++){
        iso1[s[i]].push_back(i);
        iso2[t[i]].push_back(i);
    }

    for(int i=0; i<s.length(); i++)
        if(iso1[s[i]] != iso2[t[i]])
            return false;

    return true;
}

int main() {
    // cout << isIsomorphic("aba", "xxy");
    cout << isIsomorphic("qwertyuiop[]asdfghjkl;'\\zxcvbnm,./", "',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz");
}