#include <iostream>

using namespace std;

bool isBadVersion(int version);

int firstBadVersion(int n) {
    int left = 1;
    int right = n;
    int mid;

    while(left < right){
        mid = (right - left) / 2 + left;

        if(isBadVersion(mid))
            right = mid;
        else
            left = mid+1;
    }
    return left;
}

int main(){
    cout << firstBadVersion(5);
}