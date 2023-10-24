#include<iostream>
#include<vector>

using namespace std;

pair<int, vector<int>> removeDuplicates(vector<int>& nums) {
    if (nums.size() <= 1) {
        return {nums.size(), nums};
    }

    int i = 0;
    for (int j = 1; j < nums.size(); j++) {
        if (nums[i] != nums[j]) {
            i++;
            nums[i] = nums[j]; 
        }
    }

    vector<int> unique_elements(nums.begin(), nums.begin() + i + 1); 

    return {i + 1, unique_elements};
}

int main() {
    vector<int> nums = {1, 1, 2, 2, 3, 3, 4, 5};
    pair<int, vector<int>> result = removeDuplicates(nums);

    cout<<result.first<<endl;
    for (int element : result.second) {
        cout << element << " ";
    }
    cout << endl;
}
