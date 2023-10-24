#include <iostream>


using namespace std;

bool isHappy(int n) {
    int t = n, l, sum = 0;
    while (t != 1 && t != 4) {
        sum = 0;
        while (t > 0) {
            l = t % 10;
            sum += l * l;
            t /= 10;
        }
        t = sum;
    }
    return t == 1;
}
int main() {
    cout<<isHappy(37);
}

#include<unordered_set>
bool isHappy(int n) {
    unordered_set<int> seen;

    while (n != 1) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        if (seen.find(sum) != seen.end()) {
            return false; // Cycle detected
        }
        seen.insert(sum);
        n = sum;
    }

    return true;
}

