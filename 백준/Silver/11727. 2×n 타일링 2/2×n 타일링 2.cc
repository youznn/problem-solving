#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>
#include <deque>

using namespace std;
int n;

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    int dp[1001];
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 3;
    cin >> n;

    for(int i=3; i<n+1; i++){
        dp[i] = (dp[i-2] * 2)%10007 + dp[i-1] % 10007;
    }

    cout << dp[n] % 10007;
    


}