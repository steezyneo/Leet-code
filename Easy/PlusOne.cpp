#include<iostream>
#include<vector>

using namespace std;

vector<int> plusOne(vector<int>& digits) {
    int last;
    int sum = 0;

    for(int e : digits)
        sum = sum*10 + e;
    sum++;

    vector<int> p1;

    if(sum == 10){
        digits.pop_back();
        digits.push_back(1);
        digits.push_back(0);
    }
    else{
        last = sum%10;
        digits.pop_back();
        digits.push_back(last);
    }
    return digits;
}


int main(){
    vector<int> v{9};
    auto res = plusOne(v);
    cout<<"Result: ";
    for (auto i : res)
        cout << i << " ";
}

