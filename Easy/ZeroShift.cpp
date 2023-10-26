#include <iostream>
#include <vector>


using namespace std;

void moveZeroes(vector<int>& nums) {
    int l = nums.size();
    vector<int> arr(l, 0);

    int j = 0;
    for(int i=0; i<l; i++)
        if(nums[i] != 0)
            arr[j++] = nums[i];
        
    nums = arr;
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);

    for (int num : nums) 
        cout << num << " ";
    
}