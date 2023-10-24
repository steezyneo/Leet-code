#include<iostream>
#include<vector>
#include<map>
#include<math.h>
    
    
using namespace std;

vector<int> majorityElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> eles;
    map<int, int> charfreq;

    for(int e : nums)
        charfreq[e]++;

    int ele;
    for(auto pair : charfreq){
        if(pair.second > n/3){
            eles.push_back(pair.first);
        }
    }
    
    return eles;
}

int main(){
    vector<int> v{1,2};
    for(int i : majorityElement(v))
        cout << i << " ";
}