#include<iostream>    

using namespace std;

string convertToTitle(int n) {
    string result = "";
    while (n > 0){
        n--;
        char c = 'A' + n % 26;
        result = c + result;
        n /= 26;
    }
    return result;
}

int main(){
    cout<<convertToTitle(52);
}