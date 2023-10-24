#include <bits/stdc++.h>

using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int j=0;
    for(int i=m; i<nums1.size(); i++)
        if(nums1[i] == 0){
            nums1[i] = nums2[j];
            j++;
        }
    sort(nums1.begin(), nums1.end());

}

int main() {
    vector<int> a = {1,2,3,0,0,0};
    vector<int> b = {1,2,3};
    merge(a, 3, b, 3);

    for(int x:a)
    cout<<x<<" ";
}
