#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;

//dp n < 11 
//1을 나타내는 경우 -> 1
//2를 나타내는 경우 -> 2 or dp[1] * dp[1]
//3을 나타내는 경우 -> 3 or dp[1] * dp[2] ,
//4 -> dp[1] * dp[3], dp[2] * dp[2]


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    
    int dp[12] = {0, };
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;


    for(int i=4; i<12; i++){
        //dp만들기
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    }

    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        cout << dp[N] << '\n';
    }

}