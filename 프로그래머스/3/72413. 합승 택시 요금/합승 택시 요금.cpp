#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
//8시 53분
//어피치한테 합승 제안

//'모두' 귀가하는 데 소요되는 예상 최저 택시요금???
// 다익스트라로 풀어 보자...!
// A먼저 다익스트라로 넣고,
// 이후에 B를 ??
// 그 담에 A+B를!

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    
    long long int floyd[201][201];
    fill(&floyd[0][0], &floyd[200][201], 1e9);
    
    for(int i=0; i<n+1; i++) floyd[i][i] = 0;
    
    for(auto fare:fares){
        floyd[fare[0]][fare[1]] = fare[2];
        floyd[fare[1]][fare[0]] = fare[2];
    }
    //플로이드 워셜로...?

    for(int k=1; k<n+1; k++){
        for(int i=1; i<n+1; i++){
            for(int j=1; j<n+1; j++){
                if(floyd[i][j] > floyd[i][k] + floyd[k][j]){
                    floyd[i][j] = floyd[i][k] + floyd[k][j];
                }
            }
        }
    }
    
    
    //최소 택시 요금을 구하려면...?
    //S에서 k까지의 요금 + k에서 B까지의 요금 + K에서 A까지의 요금이 최소가 되는 K 지점 찾기
    long long int taxi = floyd[s][a] + floyd[s][b];
    for(int i=1; i<n+1; i++){
        taxi = min(taxi, floyd[s][i] + floyd[i][b] + floyd[i][a]);
    }
    

    int answer = taxi;
    return answer;
}