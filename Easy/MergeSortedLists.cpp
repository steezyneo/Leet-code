#include <bits/stdc++.h>

using namespace std;

vector<int> mergeVectors(vector<int> a, vector<int> b){
    int n = a.size(), m = b.size();

    vector<int> c(n+m);
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    merge(a.begin(), a.end(), b.begin(), b.end(), c.begin());

    return c;
}

int main() {
    vector<int> a = {1,2,3,4,5};
    vector<int> b = {1,2,3};

    vector<int> c;
    c = mergeVectors(a,b);

    for(int e : c)
        cout<<e<<" ";
}
