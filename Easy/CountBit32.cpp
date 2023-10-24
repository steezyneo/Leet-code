#include <iostream>

using namespace std;

int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) { 
        count += n & 1;
        n = n >> 1;
    }
    return count;
}


int main() {
    uint32_t num = 11;  
    cout << hammingWeight(num);
}
