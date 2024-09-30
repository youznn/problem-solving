#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;

int N; //물건
int W, V; //무게 가치
int K; //배낭 크기
int bag[102][2] = {0, }; //무게, 가치
int dp[102][100001] = {0, };


int main(){
    //2시 30분
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> K;
    for(int i=1; i<N+1; i++){
        cin >> bag[i][0] >> bag[i][1];
    }

    //가치의 최댓값을 출력한다
    //i번째거를 넣는 경우의 최대. 넣지 않는 경우의 최대를 각각 구하기??... 음 ...
    for(int i=1; i<N+1; i++){
        for(int j=1; j<K+1; j++){
            //만약 해당하는 무게가 배낭 무게보다 더 클 경우에 이전 걸 담는다...?
            if(bag[i][0] > j) dp[i][j] = dp[i-1][j];
            else{
                //비교
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i][0]] + bag[i][1]);
            } 

        }
    }

    cout << dp[N][K];


}