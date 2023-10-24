#include<iostream>
#include<vector>
#include<unordered_map>
    
    
using namespace std;

int majorityElement(vector<int>& nums) {
    unordered_map<int, int> charfreq;

    for(int e : nums)
        charfreq[e]++;

    int max = INT_MIN;
    int ele;
    for(auto pair : charfreq){
        if(pair.second > max){
            max = pair.second;
            ele = pair.first;
        }
    }
    
    return ele;
}

int main(){
    vector<int> v{2,2,1,1,1,2,2};
    cout<<majorityElement(v);
}