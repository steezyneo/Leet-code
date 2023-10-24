#include <iostream>
using namespace std;

int climbStairs(int n) {
    if (n <= 2) 
        return n;  

    int steps[n+1];
    steps[1] = 1;
    steps[2] = 2;

    for (int i = 3; i <= n; i++) {
        steps[i] = steps[i-1] + steps[i-2];
    }

    return steps[n];
}

int main() {
    int n = 4;  
    cout << "Number of distinct ways to climb " << n << " steps: " << climbStairs(n) << endl;
    return 0;
}
