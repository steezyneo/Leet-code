#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int findMissingNumber(vector<int>& nums) {
    unordered_map<int, int> numMap;
    
    for (int num : nums) 
        numMap[num] = 1;
    
    for (int i = 0; i <= nums.size(); i++) 
        if (numMap.find(i) == numMap.end()) 
            return i;
    
    return -1;
}

int main() {
    vector<int> nums = {3, 7, 1, 2, 8, 4, 5};
    int missingNumber = findMissingNumber(nums);

    cout << missingNumber << endl;

    return 0;
}
