#include <iostream>
using namespace std;

int mySqrt(int x) {
    if (x == 0) 
        return 0;

    int i = 1;

    while (i <= x / i) 
        i++;    

    return i - 1;            
}

int main() {
    int n = 7;
    cout << "The square root of " << n << " is: " << mySqrt(n) << endl;
    return 0;
}
