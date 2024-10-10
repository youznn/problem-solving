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

int N, M;
int snake[101] = {0, };
int ladder[101] = {0, };
int main(){
    //15:05
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for(int i=0; i<N; i++){
        int x, y;
        cin >> x >> y;
        ladder[x] = y;
    }
        for(int i=0; i<M; i++){
        int x, y;
        cin >> x >> y;
        snake[x] = y;
    }
    //dp다 이거...
    int dp[101];
    fill(dp,dp+101,1e9);
    //1번부터 채우기
    dp[0] = 0;
    dp[1] = 0;

    // dp[i] = max(dp[i-1]+1, dp[i-2]+1, dp[i-3]+1, dp[i-4]+1, dp[i-5]+1, dp[i-6]+1, dp[i])
    // 잘 가다가 사다리가 있으면 -> dp[y] = max(dp[x], dp[y]) //여기 밞으면 무조건 올라감!!
    // 잘 가다가 뱀이 있으면 -> dp[y] = max(dp[x], dp[y])   //여기 밟으면 무조건 내려감!!

    for(int i=1; i<101; i++){
        // 가장 최단 거리 구하기
        for(int j=1; j<=6; j++){
            if(i-j >= 1){
                if(ladder[i-j]) continue;
                if(snake[i-j]) continue;
                dp[i] = min(dp[i-j] + 1, dp[i]);
            }
        }
        //사다리가 있으면
        if (ladder[i]){
            int y = ladder[i];
            dp[y] = min(dp[y], dp[i]);
        }
        //뱀
        if(snake[i]){
            int y = snake[i];
            dp[y] = min(dp[y], dp[i]);
        }
    }

    for(int i=1; i<101; i++){
        // 가장 최단 거리 구하기
        for(int j=1; j<=6; j++){
            if(i-j >= 1){
                if(ladder[i-j]) continue;
                if(snake[i-j]) continue;
                dp[i] = min(dp[i-j] + 1, dp[i]);
            }
        }
        //사다리가 있으면
        if (ladder[i]){
            int y = ladder[i];
            dp[y] = min(dp[y], dp[i]);
        }
        //뱀
        if(snake[i]){
            int y = snake[i];
            dp[y] = min(dp[y], dp[i]);
        }
    }
    cout << dp[100];

}