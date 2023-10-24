#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int maxProfit(vector<int>& prices) {
    
    int min = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.size() ; i++) {
        if (prices[i] < min) 
            min = prices[i];
        
        else{
            int profit = prices[i] - min;
            if(profit > maxProfit)
                maxProfit = profit;
        } 
        
    }

    return maxProfit;
}

int main() {
    // vector<int> prices = {7, 1, 5, 3, 6, 4};
    vector<int> prices = {7, 6, 4, 3, 1};
    // vector<int> prices = {2, 4, 1};
    // vector<int> prices = {2, 1, 4};
    cout<<maxProfit(prices);
    // maxProfit(prices);
    // cout << profit << endl;
}
