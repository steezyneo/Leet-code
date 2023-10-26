#include <iostream>
#include <vector>

using namespace std;

vector<int> luckyNumbers (vector<vector<int>>& matrix) {
    vector<int> minR;
    for(int i=0; i<matrix.size(); i++){
        int min = matrix[i][0];
        for(int j=0; j<matrix[i].size(); j++)
            if(matrix[i][j] < min){
                min = matrix[i][j];
            }
        minR.push_back(min);       
    }

    vector<int> maxC;
    for(int j=0; j<matrix[0].size(); j++){
        int max = matrix[0][j];
        for(int i=1; i<matrix.size(); i++)
            if(matrix[i][j] > max){
                max = matrix[i][j];
            }
        maxC.push_back(max);       
    }

    vector<int> lucky;
    for(int i=0; i<minR.size(); i++){
        for(int j=0; j<maxC.size(); j++){
            if(minR[i] == maxC[j] )
                lucky.push_back(minR[i]);
        }
    }
    
    return lucky;
}

int main() {
    vector<int> res;
    vector<vector<int>> arr = {{3, 7, 8}, {9, 11, 13}, {15, 16, 17}};
    res = luckyNumbers(arr);

    for(int e : res){
        cout << e << " ";
    }
}