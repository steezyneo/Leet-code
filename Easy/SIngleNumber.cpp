#include<iostream>
#include<vector>
#include<unordered_map>
    
    
using namespace std;

int singleNumber(vector<int>& nums) {
    unordered_map<int, int> freq;
    unordered_map<int, int> :: iterator p;

    for(int e : nums)
        freq[e]++;
    
    for(p = freq.begin(); p!=freq.end(); p++)
        if(p->second == 1)
            return p->first;
    return 0;
}

int main(){
    vector<int> v{2,2,1};
    cout<<singleNumber(v);
}