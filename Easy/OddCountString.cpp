#include <iostream>

using namespace std;

class Solution{
    string generateTheString(int n) {
        string res;
        if(n%2!=0){
            while(n!=0){
                res+="a";
                n--;
            }
        }
        else{
            while((n-1)!=0){
                res+="a";
                n--;
            }
            res+="b";
        }
        return res;
    }
};

int main() {
    
}