#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;

//1번집 != 2번집 
//N번집 != N-1번집 (양끝 같지 않게하기)
// i-1 != i, i!= i+1

//이중리스트???

int dp[1001][3] = {0, };
int price[1001][3];


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N; cin >> N;
    for(int i=0; i<N; i++){
        cin >> price[i][0] >> price[i][1] >> price[i][2];
    }

    //각각 해당 집이 RGB를 택했을 때의 값 저장하기
    dp[0][0] = price[0][0]; dp[0][1] = price[0][1]; dp[0][2] = price[0][2]; 
    //dp[1][0] = min(dp[0][1] + price[0][0], dp[0][2] + price[0][0]) 이전집이 G,B인 경우에서 더 작은 경우
    //dp[1][1] = min(dp[0][0] + price[0][1], dp[0][2] + price[0][1])

    for(int i=1; i<N; i++){
            //이전 집 색깔에 따라 현재 집 정해짐
            //지금 숫자 빼고 0이면 1,2 1이면 0,2 2이면 0,1
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0];
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1];
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2];
    }

    //최솟값 출력
    int min_val = 100000000;
    for(auto it: dp[N-1]){
        if(it < min_val) min_val = it;
    }
    cout << min_val;



}