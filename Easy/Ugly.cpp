#include <iostream>
#include <vector>
using namespace std;

bool isUgly(int n) {
    if(n<=0) return false;
    vector<int> prime = {2,3,5};
    for (int p : prime)
        while (n % p == 0) 
            n/=p;
    return n==1;
}

int main() {
    cout<<isUgly(40);
}