#include<iostream>

using namespace std;

int lengthOfLastWord(string s) {
    int size = s.length();
    for(int j=s.length()-1; j>=0; j--)
        if(s[j] == ' ')
            size--;
        else if (isalnum(s[j]))
            break;

    int length = 0;
    for(int i=0; i<size; i++)
        if(s[i] != ' ')
            length++;
        else
            length = 0;
    return length;
}

int main(){
    string str = "   ride  me out   ";
    cout<<lengthOfLastWord(str);
}