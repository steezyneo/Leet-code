#include<iostream>
#include<vector>

using namespace std;

vector<int> getRow(int rowIndex) {
    vector<vector <int>> res;
    res.push_back({1});
    for(int k=1; k<=rowIndex; k++){
        vector <int> temp(k+1, 1);
        for(int j=1; j<k; j++)
            temp[j] = res[k-1][j] + res[k-1][j-1];
        res.push_back(temp);
    }
    return res[rowIndex];
}
    

int main(){
    int gr;
    cin>>gr;

    vector<int> res = getRow(gr);

    for(auto e : res)
        cout<<e<<" ";
}
