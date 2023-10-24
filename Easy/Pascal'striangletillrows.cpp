#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> pascal;
    for (int i = 0; i < numRows; i++) {
        vector<int> temp(i + 1, 1);
        for (int j = 1; j < i; j++)
            temp[j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
        pascal.push_back(temp);
    }
    return pascal;
}

int main() {
    vector<vector<int>> pas(5);
    pas = generate(5);

    for (auto x : pas) {
        for (int y : x) {
            cout << y << " ";
        }
    }
}
