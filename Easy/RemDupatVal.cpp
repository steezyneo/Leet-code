#include<iostream>
#include<vector>

using namespace std;

int removeElement(vector<int>& nums, int val) {
        int k=0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
}

int main(){
    vector<int> v ={3,2,2,3};
    cout<<removeElement(v, 3);
}