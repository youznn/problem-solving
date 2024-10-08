#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;
int N;
vector<vector<int> > v;

int dr[4] = {1,-1,0,0};
int dc[4] = {0,0,1,-1};
int board[101][101] = {0, };

int bfs(int st, int en){
    queue<int > q;
    int visited[101][101] = {0, };
    q.push(st);
    int flag = 0;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        
        if( cur == en ){
            //cout << "now" << ' ' << cur << '\n';
            if(st == en && !flag) {
                flag = 1;
            } else {
                return 1;
            }
        }
        
        for(int i=0; i<N; i++){
            if (board[cur][i] && !visited[cur][i]){
                //cout << "next " << i << '\n';
                visited[cur][i] = 1;
                q.push(i);
            }
        }

    }
    return 0;

}

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            int n;
            cin >> n;
            board[i][j] = n;
        }
    }

    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cout << bfs(i,j) << ' ';
        }
        cout << '\n';
    }





}