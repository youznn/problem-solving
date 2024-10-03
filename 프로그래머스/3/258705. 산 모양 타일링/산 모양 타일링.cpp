#include <string>
#include <vector>

using namespace std;
//11:50
//dp같음... 뭔가
//dp[0][1] dp[0][0] //1은 왼쪽아래로가는 평.사 있을 때
//dp[1][1] = dp[0][0] + dp[0][1]
//dp[1][0] = dp[0][0] * 3(2) + dp[0][1] * 2(1)

int dp[100001][3];
int solution(int n, vector<int> tops) {
    
    dp[0][0] = 1;
    dp[0][1] = 0;
    
    for(int i=1; i<n+1; i++){
        int k;
        if(tops[i-1]) k = 3; else k = 2;
        dp[i][1] = dp[i-1][0] % 10007 + dp[i-1][1] % 10007;
        dp[i][0] = dp[i-1][0] * k % 10007 + dp[i-1][1] * (k-1) % 10007;
    }
    
    int answer = (dp[n][0] + dp[n][1]) % 10007;
    return answer;
}