#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> removeDuplicates(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    return nums;
}

int main() {
    vector<int> nums = {1, 1, 1, 2, 2, 3, 4, 4, 5};
    removeDuplicates(nums);
    for (int x : nums){
        cout << x << " ";
    }
}
